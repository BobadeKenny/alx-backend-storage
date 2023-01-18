#!/usr/bin/env python3
""" 9-insert_school.py """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    if mongo_collection:
        return mongo_collection.insert_one(kwargs).inserted_id
    else:
        return None