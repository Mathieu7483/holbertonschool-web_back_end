#!/usr/bin/env python3
"""Function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic: The topic to search for.

    Returns:
        A list of school documents that have the specified topic.
    """
    schools = mongo_collection.find({'topics': topic})
    return list(schools)
