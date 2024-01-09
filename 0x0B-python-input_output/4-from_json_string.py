#!/usr/bin/python3
# 6-from_json_string.py
"""JSON to object"""
import json


def from_json_string(my_str):
    """JSON string"""
    return json.loads(my_str)
