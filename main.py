from ctypes.wintypes import HANDLE

import win32file


class PipeClient:

    def __init__(self, name: str):
        self.__name = name

    def send_message(self, message: str) -> None:
        print("writing from client")
        handle = self.__connect_to_pipe()
        win32file.WriteFile(handle, message)

    def receive_message(self) -> None:
        print("reading from client")
        handle = self.__connect_to_pipe()
        _, data = win32file.ReadFile(handle, 200)
        print(data)

    def __connect_to_pipe(self) -> HANDLE:
        file_handle = win32file.CreateFile(
            f"\\\\.\\pipe\\{self.__name}",
            win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0,
            None,
            win32file.OPEN_EXISTING,
            0,
            None)
        return file_handle


client = PipeClient(name="test-pipe")

while (True):
    command = input()
    command_parts = command.split("#")
    if command_parts[0] == "0":
        client.receive_message()
    elif command_parts[0] == "1":
        client.send_message(command_parts[1])
