"""
JSON Parsing Demo in Python
This script demonstrates how to parse JSON data and convert Python objects to JSON.
"""

import json

# Sample JSON string (as received from an API)
json_string = '''
{
    "id": 1,
    "title": "The Great Gatsby"
}
'''

# Parse JSON string to Python dictionary
book = json.loads(json_string)

print(book['title'])

# Convert Python dictionary back to JSON string
json_output = json.dumps(book, indent=4)
print("\nModified JSON:")
print(json_output)