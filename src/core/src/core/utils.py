import json
import datetime

def pretty_json(data):
    """Return formatted JSON for readability."""
    return json.dumps(data, indent=2)

def timestamp():
    """Return a simple timestamp string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def safe_get(d, key, default=None):
    """Safely get a key from a dict with a default."""
    return d[key] if key in d else default
import os

def mock_mode():
    return os.getenv("MOCK_MODE", "false").lower() == "true"
