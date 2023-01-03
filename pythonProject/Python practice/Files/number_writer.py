import json

number = [2, 3, 4, 6, 8, 11, 15]
filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
