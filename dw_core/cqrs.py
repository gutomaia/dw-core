"""CQRS (Command Query Responsibility Segregation) base classes.

This module provides the foundational classes for implementing the CQRS pattern.
It separates the command-side (write operations) from the query-side (read operations)
of the system.
"""

from pydantic import BaseModel

__all__ = ['Command', 'Query', 'Event']


class CQRSRequest(BaseModel):
    """Base class for all CQRS requests.

    This class extends Pydantic's BaseModel to provide validation and serialization
    capabilities for all CQRS requests.
    """

    pass


class CQRSResponse(BaseModel):
    """Base class for all CQRS responses.

    This class extends Pydantic's BaseModel to provide validation and serialization
    capabilities for all CQRS responses.
    """

    pass


class Command(CQRSRequest):
    """Base class for command requests in CQRS pattern.

    Commands represent intentions to change the system state. They are named with
    imperative verbs and should be processed exactly once. Examples include:
    CreateUser, UpdateProfile, DeleteAccount.
    """

    pass


class Query(CQRSResponse):
    """Base class for query responses in CQRS pattern.

    Queries represent requests for information that do not modify system state.
    They can be executed multiple times without side effects. Examples include:
    GetUserProfile, ListOrders, SearchProducts.
    """

    pass


class Event(BaseModel):
    """Base class for domain events in CQRS pattern.

    Events represent facts that have occurred in the system. They are named in
    past tense and are immutable. Examples include: UserCreated, OrderPlaced,
    EmailSent.
    """

    pass
