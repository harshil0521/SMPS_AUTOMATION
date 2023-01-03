colours = ['White', 'Black', 'Yellow', 'Green', 'maroon', 'Violet']
print(colours[3].upper())
print(colours[-1])
colours[3] = 'Purple'
print(colours[3])

# Appending elements to the end of list
colours.append('Orange')
print(colours)
shapes = []
print(shapes)
shapes.append("Square")
print(shapes)

# Appending elements to the end of list
colours.insert(0, "Blue")
print(colours)

# Removing element from list
del colours[1]
print(colours)

# Removing element from list
walls = ['col_1', 'col_2', 'col_3', 'col_4']
print(walls)
popp_wall = walls.pop(-2)
print(walls)

# Removing element from list
walls = ['wall_1', 'wall_2', 'wall_3', 'wall_4']
print(walls)
walls.remove('wall_1')
print(walls)

walls = ['wall_1', 'wall_2', 'wall_3', 'wall_4']
print(walls)
second = 'wall_2'
walls.remove(second)
print(walls, "\n")

# sorting in list
print(colours)
colours.sort()
print(colours)

colours.sort(reverse=True)
print(colours)

print(sorted(colours))

colours.reverse()
print(colours)

# Length of list
name = ['Harshil', 'Deep', 'Pratik']
print(len(name))
