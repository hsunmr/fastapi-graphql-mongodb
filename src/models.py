import strawberry
from typing import List, Optional

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

@strawberry.type
class PageMeta:
    next_cursor: Optional[str] = strawberry.field(
        description="The next cursor to continue with."
    )

@strawberry.type
class PostsResponse:
    posts: List[Post] = strawberry.field(
        description="The list of posts."
    )
    page_meta: PageMeta = strawberry.field(
        description="Metadata to aid in pagination."
    )

@strawberry.type
class CreatePostResponse:
    id: str

@strawberry.type
class UpdatePostResponse:
    id: str

@strawberry.type
class DeletePostResponse:
    message: str = "Post deleted"