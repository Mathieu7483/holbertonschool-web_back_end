#!/usr/bin/env python3
"""Improve 12-log_stats.py by adding the top 10 of the most present
IPs in the collection nginx of the database logs"""
from pymongo import MongoClient


def log_stats():
    """Provides statistics about Nginx logs."""
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")


    status_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f"{status_count} status check")

    ips_sequence = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ]
    top_ips = nginx_collection.aggregate(ips_sequence)
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")



if __name__ == "__main__":
    log_stats()