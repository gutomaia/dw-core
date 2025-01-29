from pydantic import BaseModel

__all__ = ['Command', 'Query', 'Event']


class CQRSRequest(BaseModel):
    pass


class CQRSResponse(BaseModel):
    pass


class Command(CQRSRequest):
    pass


class Query(CQRSResponse):
    pass


class Event(BaseModel):
    pass
