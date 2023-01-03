import json

filename = 'number.json'
with open(filename) as obj:
    numbers = json.load(obj)

print(numbers)
