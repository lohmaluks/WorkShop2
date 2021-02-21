import json

# a Python object (dict):
python_dict = {"name": "Hanbin & Ying", "age": 23, "city": "Vietnam"}

# convert into JSON:
json_string = json.dumps(python_dict)

# the result is s JSON string:
print(json_string)