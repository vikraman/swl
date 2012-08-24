
import json

def serialize(obj):
    return json.JSONEncoder().encode(obj)
