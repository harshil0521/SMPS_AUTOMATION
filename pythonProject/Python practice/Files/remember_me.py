import json
filename = "username.json"

with open(filename, 'w') as obj:
    for i in range(10):
        user_name = input("What is your name? ")
        json.dump(user_name, obj)
