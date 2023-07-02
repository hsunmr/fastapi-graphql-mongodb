import typing
import strawberry
from strawberry.types import Info
from models import Post, PostsResponse, CreatePostResponse, UpdatePostResponse, DeletePostResponse
from inputs import AuthorInput
from resovlers import get_posts, get_post, create_post, update_post, delete_post



@strawberry.type
class Query:
    @strawberry.field
    def posts(self, info: Info, limit: int, cursor: typing.Optional[str] = None) -> PostsResponse:
        posts = get_posts(info, limit, cursor)
        return posts

    @strawberry.field
    def post(self, info: Info, post_id: str) -> typing.Optional[Post]:
        post = get_post(post_id, info)
        return post

@strawberry.type
class Mutation:
    @strawberry.mutation
    def post(self, title: str, content: str, author: AuthorInput) -> CreatePostResponse:
        return create_post(title, content, author)
    @strawberry.mutation
    def update_post(self, post_id: str, title: str, content: str, author: AuthorInput) -> UpdatePostResponse:
        return update_post(post_id, title, content, author)
    @strawberry.mutation
    def delete_post(self, post_id: str) -> DeletePostResponse:
        return delete_post(post_id)