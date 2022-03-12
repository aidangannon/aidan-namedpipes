from core import PipeClient, Logger
from crosscutting import PythonLogger
from data import Win32PipeClient

logger: Logger = PythonLogger()
client: PipeClient = Win32PipeClient(name="test-pipe", logger=logger)

while True:
    try:
        command = input()
        command_parts = command.split("#")
        if command_parts[0] == "0":
            client.receive_message()
        elif command_parts[0] == "1":
            client.send_message(command_parts[1])
    except Exception as e:
        logger.log_error(str(e))
