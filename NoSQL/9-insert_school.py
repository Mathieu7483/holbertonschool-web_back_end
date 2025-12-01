#!/usr/bin/env python3
""" Function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs representing the document fields and values.
    Returns:
        The inserted document's ID.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
