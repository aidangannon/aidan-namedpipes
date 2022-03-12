using Aidan.NamedPipes;

var state = new InteractivePipeState( );
var pipe = new PipeServer( "test-pipe", state );

pipe.Start(  );

while( true )
{
    var command = Console.ReadLine( );
    var inputState = command.Split( "#" );
    switch( inputState[ 0 ] )
    {
        case "0":
            state.ReadOrWrite = false;
            break;
        case "1":
            state.ReadOrWrite = true;
            state.WriteMessage = inputState[ 1 ];
            break;
    }
}

