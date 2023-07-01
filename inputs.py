import strawberry
import typing

@strawberry.input
class AuthorInput:
    name: str
    email: typing.Optional[str] = None