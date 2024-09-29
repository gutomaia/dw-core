from pydantic import BaseModel

__all__ = ['Command', 'Query', 'Event']


class CQRSRequest(BaseModel):
    pass


class CQRSResponse(BaseModel):
    pass


class Command(BaseModel):
    pass


class Query(BaseModel):
    pass


class Event(BaseModel):
    pass
