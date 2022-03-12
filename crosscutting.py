class PythonLogger:

    def log_info(self, message: str) -> None:
        print(f"INFO: {message}")

    def log_error(self, message: str) -> None:
        print(f"ERROR: {message}")