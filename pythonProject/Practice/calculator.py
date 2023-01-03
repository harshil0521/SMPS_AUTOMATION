def cal_fun():
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    operation = int(input("Enter your choice : "))
    if operation == 1:
        first_val = input("Enter first value : ")
        second_val = input("Enter second value : ")
        print('Your answer is ', int(first_val) + int(second_val))
    elif operation == 2:
        first_val = input("Enter first value : ")
        second_val = input("Enter second value : ")
        print('Your answer is ', int(first_val) - int(second_val))
    elif operation == 3:
        first_val = input("Enter first value : ")
        second_val = input("Enter second value : ")
        print('Your answer is ', int(first_val) * int(second_val))
    elif operation == 4:
        first_val = input("Enter first value : ")
        second_val = input("Enter second value : ")
        print('Your answer is ', int(first_val) / int(second_val))
    else:
        print('Please choose correct option')
