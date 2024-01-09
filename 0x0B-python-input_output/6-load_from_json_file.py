#!/usr/bin/python3
"""JSON read"""
import json


def load_from_json_file(filename):
    """JSON file"""
    with open(filename) as f:
        return json.load(f)
