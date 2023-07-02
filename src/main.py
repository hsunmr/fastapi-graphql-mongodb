from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from schemas import Query,Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)

def create_app():
    app = FastAPI()
    graphql_app = GraphQLRouter(schema)
    app.include_router(graphql_app, prefix="/graphql")
    return app
