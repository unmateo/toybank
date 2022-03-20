from fastapi import HTTPException


class HandledException(HTTPException):

    message = "Ups! There was an unexpected error"
    status_code = 500

    def __init__(self, detail=None):
        super().__init__(status_code=self.status_code, detail=detail or self.message)


class NotFound(HandledException):
    message = "Resource not found"
    status_code = 404
