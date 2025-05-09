from aiogram.fsm.state import State

class BaseError(Exception):
    def __init__(self, message: str, state: State | None = None):
        self.message = message
        self.state = state
        super().__init__(message)

class ValidationError(BaseError):
    pass