#!/usr/bin/env python3
""" 101-students.py """
import pymongo


def top_students(mongo_collection):
    """ returns all students sorted by average score """
    if mongo_collection:
        return mongo_collection.aggregate([
            {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore": -1}}
        ])
    else:
        return []
