#!/usr/bin/env python3

from pymongo import MongoClient
import os

# connect to mongo
MONGOUSER = os.getenv('MONGOUSER')
MONGOPASS = os.getenv('MONGOPASS')
MONGOHOST = os.getenv('MONGOHOST')
client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

# connect to db
thisdb = client.wka4sp

# create a new collection
pokemon_collection = thisdb.collection

# insert five (5) documents
doc1 = {
    "name":"Piplup",
    "number":393,
    "type":"water",
    "region":"Sinnoh"
}

doc2 = {
    "name":"Snivy",
    "number":495,
    "type":"grass",
    "region":"Unova"
}

doc3 = {
    "name":"Tepig",
    "number":498,
    "type":"fire",
    "region":"Unova"
}

doc4 = {
    "name":"Oshawott",
    "number":501,
    "type":"water",
    "region":"Unova"
}

doc5 = {
    "name":"Popplio",
    "number":728,
    "type":"water",
    "region":"Alola"
}

pokemon_collection.insert_many([doc1, doc2, doc3, doc4, doc5])

# write a query that displays exactly three (3) of those documents
query = pokemon_collection.find({"region": "Unova"})
print(f"Unovan Starters:\n{query}")