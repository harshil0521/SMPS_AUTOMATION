# name = input('What is your name? ').title()
# gender = input("Please enter your gender: ").title()
# if gender == 'Male':
#    print("Hello Mr. "+name)
# elif gender == 'Female':
#    print("Hello Miss "+name)
# else:
#    print("Hello "+name)
# import prompt as prompt

# age = input('Please enter your age : ')
# print(age)


# Modulo operator

# rem = 4 % 3
# print(rem)

# number = input("Please enter a number, and I'll tell you if it is even or odd : ")
# number = int(number)
# if number % 2 == 0:
#    print(str(number)+" is even number.")
# else:
#    print(str(number)+" is odd number.")

# While Loops

# num = 1
# while num < 5:
#    print(num, 'is less than 5')
#    num += 1

# game = "Let's start the game"
# print(game)
# choice = ""
# while choice != 'no':
#    choice = input()
#    print(choice)


# Flag

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#    message = input(prompt)
#    if message == 'quit':
#        print('Thanks for playing')
#        active = False
#    else:
#        print(message)

# while True:
#    city = input(prompt)
#
#    if city == 'quit':
#        break
#    else:
#        print("I love to go " + city.title())

# digit = 0
# while digit < 11:
#    digit += 1
#    if digit % 2 == 0:
#        continue
#    print(digit)


# moving items from one list to another list
# unconfirmed_users = ['Savan', 'Ravi', 'Ankit', 'Kandarp']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user : " + current_user.title())
#     confirmed_users.append(current_user)
# print('\nVerified user are as following :')
# for confirmed_user in confirmed_users:
#     print(confirmed_user)

# for i in range(1, 11):
#    print(i*i)
#    i += 1

# removing all instance of same values

# pets = ['cat', 'dog', 'turtle', 'fish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

responses = {}
polling_activity = True
while polling_activity:
    name = input('Enter name : ')
    response = input('Desired destination : ')
    responses[name] = response
    repeat = input('Is there any next person ? (yes/no) : ').title()
    if repeat == 'No':
        polling_activity = False
print(responses)

for name, response in responses.items():
    print(name.title() + " would like to go to " + response + '.')

digit = 0
while digit < 11:
    digit += 1
    print(digit)
