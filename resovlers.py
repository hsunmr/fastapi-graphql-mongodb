from db import db
from models import Post,Author
from inputs import AuthorInput
from bson.objectid import ObjectId

def get_posts(info):
    posts = db.posts.find()

    return [
        Post(
            id=post['_id'],
            title=post['title'],
            content=post['content'],
            author=Author(
                name=post['author']['name'],
                email=post['author']['email']
            )
        ) for post in posts
    ]

def get_post(post_id, info):
    post = db.posts.find_one({
        "_id": ObjectId(post_id)
    })

    result = None

    if post:
        result = Post(
            id=post['_id'],
            title=post['title'],
            content=post['content'],
            author=Author(
                name=post['author']['name'],
                email=post['author']['email']
            )
        )

    return result

def create_post(title: str, content: str, author: AuthorInput) -> Post:
    post = db.posts.insert_one({
        'title': title,
        'content': content,
        'author': {
            'name': author.name,
            'email': author.email
        }
    })

    inserted_id = post.inserted_id

    return Post(
        id=inserted_id,
        title=title,
        content=content,
        author=Author(
            name=author.name,
            email=author.email
        )
    )
