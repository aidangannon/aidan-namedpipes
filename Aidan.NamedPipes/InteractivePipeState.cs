using System.ComponentModel;

namespace Aidan.NamedPipes;

public class InteractivePipeState
{
    private bool _readOrWrite;
    public event Action<bool, string> _request;
    
    [ Description("false = read, true = write") ]
    public bool ReadOrWrite
    {
        get => _readOrWrite;
        set
        {
            _readOrWrite = value;
            _request.Invoke( ReadOrWrite, WriteMessage );
        }
    }

    public string WriteMessage { get; set; }
}