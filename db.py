import pymongo
from os import getenv
from dotenv import load_dotenv
load_dotenv()

client = pymongo.MongoClient(
    getenv("MONGO_HOST", default='localhost'),
    int(getenv("MONGO_PORT", default=27017)),
    username= getenv("MONGO_USERNAME", default='root'),
    password= getenv("MONGO_PASSWORD", default='root')
)

MONGO_DATABASE = getenv("MONGO_DATABASE", default="blog")

db = client[MONGO_DATABASE]
