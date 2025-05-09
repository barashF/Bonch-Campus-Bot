class BaseError(Exception):
    def __init__(self, message: str, state: str = None):
        self.message = message
        self.state = state
        super().__init__(message)

class ValidationError(Exception):
    pass