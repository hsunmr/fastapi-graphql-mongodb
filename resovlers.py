from db import db
from models import Post, Author, PageMeta, PostsResponse
from inputs import AuthorInput
from bson.objectid import ObjectId
from heplers import decode_user_cursor, encode_user_cursor

def get_posts(info, limit, cursor):
    filter = {
        "_id": {
            "$gt": ObjectId(decode_user_cursor(cursor=cursor))
        }
    } if cursor else {}

    posts = list(db.posts.find(filter).limit(limit))

    post_data = []
    for post in posts:
        post_data.append(
            Post(
                id=post['_id'],
                title=post['title'],
                content=post['content'],
                author=Author(
                    name=post['author']['name'],
                    email=post['author']['email']
                )
            )
        )

    last_post = db.posts.find_one({}, {"_id": 1}, sort=[("_id", -1)])

    if (len(posts) > 0):
        next_cursor = encode_user_cursor('post', posts[-1]['_id'])
        for post in posts:
            if post['_id'] == last_post['_id']:
                next_cursor = None
                break
    else:
        next_cursor = None

    return PostsResponse(
        posts=post_data,
        page_meta=PageMeta(
            next_cursor=next_cursor
        )
    )

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
