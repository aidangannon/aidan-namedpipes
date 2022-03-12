using System.IO.Pipes;
using System.Text;

namespace Aidan.NamedPipes;

public class PipeServer
{
    private readonly string _name;
    private readonly InteractivePipeState _interactivePipeState;
    private NamedPipeServerStream _pipeServer;

    public PipeServer( string name, InteractivePipeState interactivePipeState )
    {
        _name = name;
        _interactivePipeState = interactivePipeState;
    }

    public void Start( )
    {
        Task.Run( ( ) =>
        {
            while( true )
            {
                _pipeServer = new NamedPipeServerStream( _name, PipeDirection.InOut, 10 );
                Console.WriteLine("server waiting for connection");
                _pipeServer.WaitForConnection();
                Console.WriteLine("client connection accepted");
                try
                {
                    if( !_interactivePipeState.ReadOrWrite )
                    {
                        Console.WriteLine("server reading");
                        var bytes = new byte[ 200 ];
                        _pipeServer.Read( bytes );
                        Console.WriteLine( Encoding.UTF8.GetString( bytes ) );
                    }
                    else
                    {
                        Console.WriteLine("server writing");
                        _pipeServer.Write( Encoding.UTF8.GetBytes( _interactivePipeState.WriteMessage ) );
                    }
                }
                catch (IOException e)
                {
                    Console.WriteLine("ERROR: {0}", e.Message);
                }

                _pipeServer.Close( );
            }
        } );
    }
}