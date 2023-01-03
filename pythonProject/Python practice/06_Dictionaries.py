student_1 = {'gender': 'Male', 'Roll number': 4001, 'Name': 'Rahul Jain'}
student_2 = {'gender': 'Female', 'Roll number': 4002, 'Name': 'Khushi Singh'}
student_3 = {}
print(student_1['Name'])
print(student_2['Roll number'])

# Adding item into dictionary

student_3['gender'] = 'Male'
print(student_3['gender'])
print(student_3)
student_3['Roll number'] = 4003
print(student_3)
student_3['Name'] = 'Arjun Kapoor'
print(student_3)

# Modifying values in dictionary

# student_3['Roll number'] = student_1['Roll number'] + 5
# print(student_3)

# Removing key value pairs from dictionary
# del student_3['gender']
# print(student_3)


favorite_bike = {
                'harshil': 'FZS',
                'savan': 'apache',
                'naiya': 'activa',
                'ravi': 'pulser'
                }
print("Harshil's favorite_bike is " + favorite_bike['harshil'].upper() + ".")


# Looping through key-value pairs

user_0 = {'Name': 'Harshil',
          'Age': '23',
          'Gender': 'Male',
          }
for k, v in user_0.items():
    print('\nKey: ' + k)
    print('Value: ' + v)
print('\n')


for i, j in favorite_bike.items():
    print(i.title() + "'s favorite bike is " + j.upper() + '.')

for bike in favorite_bike.values():
    print(bike.upper())

friends = ['harshil', 'savan']

for name in favorite_bike.keys():
    print(name.title())
    if name in friends:
        print("\tHey " + name.title() + ", I see your favorite bike is " + favorite_bike[name], '.')
print('\n')

# Sorting filter in Dictionary using loop
for name in sorted(favorite_bike.keys()):
    print(name.title()+", Thanks you.")

for value in favorite_bike.values():
    print(value.upper(), 'is listed in favorite bike list.')

favorite_languages = {
                      'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                     }

for language in favorite_languages.values():
    print(language)
print('\n')

# Unique values only
for language in set(favorite_languages.values()):
    print(language.title())

student = [student_1, student_2, student_3]

for s in student:
    print(s)

workers = []
for worker_num in range(30):
    new_worker = {'name': 'Harshil', 'salary': '25000'}
    workers.append(new_worker)
for worker in workers[:5]:
    print(worker)

# A List in Dictionary

pizza = {
         'crust': 'thick',
         'toppings': ['mushroom', 'capsicum', 'olives']
        }
print("You ordered a " + pizza['crust'] + '-crust pizza with the following toppings.')
for top in pizza['toppings']:
    print('\t', top)

# A Dictionary in Dictionary

user = {
        'john': {
                'movie': '32',
                'status': 'married',
                'height': "6'1",
                },
        'katrina': {
                    'movie': '38',
                    'status': 'married',
                    'height': "5'7",
                   },
        }

for user_name, user_info in user.items():
    print("\nUser name : " + user_name.title())
    print("Number of movies : ", user_info['movie'], " & Height is "+user_info['height']+'.')
    print("Status of user is : ", user_info['status'].upper())

