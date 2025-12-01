#!/usr/bin/env python3
"""Function that changes all topics of a school document based on the name."""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name.

    Args:
        mongo_collection: The pymongo collection object.
        name: The name of the school to update.
        topics: The list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
    return None
