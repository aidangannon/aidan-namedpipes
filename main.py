import win32file

class PipeClient:
    
    def send_message(self, message: str) -> None:
        fileHandle = win32file.CreateFile(
            "\\\\.\\pipe\\Demo",
            win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0,
            None,
            win32file.OPEN_EXISTING,
            0,
            None)
        left, data = win32file.ReadFile(fileHandle, 4096)
        print(data)  # "hello"

while(True):
    print("")