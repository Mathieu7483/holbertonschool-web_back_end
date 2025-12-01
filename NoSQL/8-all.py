#!/usr/bin/env python3
"""Module that lists all documents in a collection."""


def list_all(mongo_collection):
    """Function that lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents in the collection.
    """
    return list(mongo_collection.find())
