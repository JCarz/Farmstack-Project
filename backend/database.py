from model import Todo

#MongoDB Driver
import motor.motor_asyncio

#AsyncIOMotorClient is a class that connects to a MongoDB server
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')

database = client.TodoList
collection = database.todo

async def fetch_one_todo(title):
    document = await collection.find_one({'title': title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos
#This is any data we are retrive and we return everything in that collection

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title, description):
    await collection.update_one({"title": title}, {"$set": {"description": description}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True