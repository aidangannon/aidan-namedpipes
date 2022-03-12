from ctypes.wintypes import HANDLE

import win32file

from core import Logger


class Win32PipeClient:

    def __init__(self,
                 name: str,
                 logger: Logger):
        self.__logger = logger
        self.__name = name

    def send_message(self, message: str) -> None:
        self.__logger.log_info("writing from client")
        handle = self.__connect_to_pipe()
        win32file.WriteFile(handle, message)

    def receive_message(self) -> None:
        self.__logger.log_info("reading from client")
        handle = self.__connect_to_pipe()
        _, data = win32file.ReadFile(handle, 200)
        self.__logger.log_info(data)

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