from pydantic import Field

from dw_core.cqrs import Command

__all__ = ['CommandAccept', 'CommandExecuted']


class CommandAccept(Command):   # status code 202
    accepted: bool = Field(
        title='Command Accepted',
        description='Defines the acceptance of the command',
        example='True/False',
    )


class CommandExecuted(Command):   # status code 200
    accepted: bool = Field(
        title='Command Accepted',
        description='Defines the acceptance of the command',
        example='True/False',
    )
