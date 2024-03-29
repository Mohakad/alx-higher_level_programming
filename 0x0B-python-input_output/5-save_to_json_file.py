#!/usr/bin/python3
"""JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Write to txt"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
