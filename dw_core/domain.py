"""Domain-specific command responses.

This module provides standard response classes for command handling in the CQRS pattern.
These responses are used to indicate the status of command processing.
"""

from pydantic import Field

from dw_core.cqrs import Command

__all__ = ['CommandAccept', 'CommandExecuted']


class CommandAccept(Command):  # status code 202
    """Response indicating that a command has been accepted for processing.

    This response is typically used in asynchronous command processing scenarios
    where the command is queued for later execution. Maps to HTTP 202 Accepted.

    Attributes:
        accepted (bool): Indicates whether the command was accepted for processing.
            Example: True if the command was accepted, False otherwise.
    """

    accepted: bool = Field(
        title='Command Accepted',
        description='Defines the acceptance of the command',
        example='True/False',
    )


class CommandExecuted(Command):  # status code 200
    """Response indicating that a command has been successfully executed.

    This response is used when a command has been fully processed and completed.
    Maps to HTTP 200 OK.

    Attributes:
        accepted (bool): Indicates whether the command was successfully executed.
            Example: True if the command was executed, False otherwise.
    """

    accepted: bool = Field(
        title='Command Accepted',
        description='Defines the acceptance of the command',
        example='True/False',
    )
