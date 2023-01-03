colours = ['white', 'black', 'blue', 'green', 'red']
for colour in colours:
    if colour == 'black':
        print(colour.upper())
    else:
        print(colour.lower())
if colours[1].lower() == 'black':
    print('yeah')
else:
    print('nahh')

if colours[1] != 'blue':
    print('Correct logic')
if colours[0] == 'white' or colours[1] == 'blue':
    print('Correct')
else:
    print('wrong')

if 'white' in colours:
    print('yes it is')

age = int(input('Please enter your age : '))
if age < 4:
    print('Free admission')
elif age <= 18:
    print('5/- for Admission')
else:
    print('10/- for Admission')
