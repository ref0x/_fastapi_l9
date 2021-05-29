import asyncio
from pprint import pprint

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

db = client.test_database
collection = db['test_collection']

async def do_insert():
	document = {'second request': '123', 'second request_2': 456}
	result = await db.test_collection.insert_one(document)
	print('result %s' % repr(result.inserted_id))


async def do_find_one():
	document = await db.test_collection.find_one()
	pprint(document)


async def do_find():
	document = db.test_collection.find().sort('i')
	for i in await document.to_list(length=100):
		pprint(i)


loop = asyncio.get_event_loop()
loop.run_until_complete(do_find_one())
