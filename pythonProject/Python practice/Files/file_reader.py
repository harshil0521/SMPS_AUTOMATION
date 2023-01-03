#with open('pi_digit') as file_object:
#    contents = file_object.read()
#pi_string = ''
#for line in contents:
#    pi_string += line.rstrip()

#birthday = input("Please enter your birthdate in ddmmyy format : ")
#if birthday in pi_string:
#    print("Yes")
#else:
#    print("No")


file_path = "C:/Users/Prerna Singh/PycharmProjects/pythonProject/Automation/digits.txt"
with open(file_path, 'w') as object_1:
    object_1.write('222')
#    num = object_1.read()
#    print(num)

with open('phone_number', 'a') as number:
    number.write('\nhey there, ')
    name = input("Enter your name: ")
    number.write(name.title())
    print(name)


try:
    print(5/0)
except ZeroDivisionError:
    print("You can divide by zero!")

