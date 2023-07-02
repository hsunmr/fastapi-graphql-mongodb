### FastAPI + GraphQL + MongoDB
| Use fastapi mongodb to implement graphql api

### Install
1 ) Set env file
```
cd src

cp .env.example .env

# set env file
# MONGO_HOST=127.0.0.1
# MONGO_PORT=27017
# MONGO_USERNAME=root
# MONGO_PASSWORD=root
# MONGO_DATABASE=blog
```

2 ) Up docker containers
```
docker-compose up -d
```
### Usage

You can access http://127.0.0.1:8000/graphql

- posts list
    ```
    query MyQuery {
        posts(limit: 10, cursor: "") {
            pageMeta {
                nextCursor
            }
            posts {
                author {
                    email
                    name
                }
                content
                id
                title
            }
        }
    }
    ```
- show post
    ```
    query MyQuery {
        post(postId: "64a03d9dc2a7309a1fdf6cdd") {
            author {
                email
                name
            }
            content
            id
            title
        }
    }
    ```
- create post
    ```
    mutation MyMutation {
        post(author: {name: "raymond", email: "test@test.com"}, content: "content", title: "title") {
            id
        }
    }
    ```
- update post
    ```
    mutation MyMutation {
        updatePost(author: {name: "name", email: "email@test.com"}, content: "changed", postId: "64a14332398ced1f632fe9af", title: "changed") {
            id
        }
    }
    ```
- delete post
    ```
    mutation MyMutation {
        deletePost(postId: "64a14332398ced1f632fe9af") {
            message
        }
    }
    ```