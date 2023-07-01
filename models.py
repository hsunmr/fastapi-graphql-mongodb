import strawberry

@strawberry.type
class Post:
    id: str
    title: str
    content: str
    author: "Author"

@strawberry.type
class Author:
    name: str
    email: str