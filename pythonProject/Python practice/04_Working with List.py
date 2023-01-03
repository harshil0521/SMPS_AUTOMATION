# loop
# cars = ['BMW', 'Audi', 'Toyota', 'Mclaren']
# for car in cars:
#    print(car.upper())

# for value in range(1, 6):
#    print(value)

num1 = list(range(1, 11))
print(num1)

num2 = list(range(1, 11, 2))
print(num2)

num3 = list(range(2, 11, 2))
print(num3)

squares = []
for value in range(1, 11):
    res = value**2
    squares.append(res)
print(squares)

cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
print(cubes)

roots = []
for value in range(2, 11, 2):
    root = int(value/2)
    roots.append(root)
print(roots)


cubes = [value**3 for value in range(1, 11)]
print(cubes)


# statistics

digits = [1, 2, 3, 4, 5]
print(min(digits))
print(max(digits))
print(sum(digits))


# slicing
friend = ['harshil', 'deep', 'meet', 'pratik', 'bittu', 'hardik', 'dhaval', 'parth', 'divy', 'dhruv']
print(friend)
length = len(friend)
for value in range(0, length):
    print(friend[value].title())
print(friend[3:7])
print(friend[:4])
print(friend[3:])
print(friend[-3:])

for fri in friend[:4]:
    print(fri.title())

close_friend = friend[3:8]
print(close_friend)

# tuple

new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(new_tuple)
for value in new_tuple:
    print(value)
new_tuple = (11, 12, 13, 14, 15)
print(new_tuple)




