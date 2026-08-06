Getting Started
===============

Installation
------------

You can install Downwind Core using pip:

.. code-block:: bash

   pip install dw-core

Basic Usage
-----------

The module is built around the CQRS pattern. Here's a basic example:

.. code-block:: python

   from dw_core.cqrs import Command, Query
   from dw_core.domain import CommandAccept

   # Define a command
   class CreateUserCommand(Command):
       username: str
       email: str

   # Handle the command
   def handle_create_user(command: CreateUserCommand) -> None:
       # Your implementation here
       pass

Entry Points
------------

Downwind Core uses entry points for extensibility. You can define your own entry points in your ``pyproject.toml``:

.. code-block:: toml

   [project.entry-points."domain"]
   user = "myapp.domain:user_domain"

   [project.entry-points."ports"]
   user_api = "myapp.ports:user_api"
