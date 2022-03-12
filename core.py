from typing import Protocol, Any


class Logger(Protocol):

    def log_info(self, message: str) -> None:
        ...

    def log_error(self, message: str) -> None:
        ...

class PipeClient(Protocol):

    def send_message(self, message: str) -> None:
        ...

    def receive_message(self) -> None:
        ...

    def __connect_to_pipe(self) -> Any:
        ...