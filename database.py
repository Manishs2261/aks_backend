from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL, DB_NAME, PRODUCTS_COLLECTION_NAME, USERS_COLLECTION_NAME

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]

products_collection = db[PRODUCTS_COLLECTION_NAME]
users_collection = db[USERS_COLLECTION_NAME]
