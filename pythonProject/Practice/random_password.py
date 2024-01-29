import secrets
import string

ul_case = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
digits = string.digits
for k in range(10000):
    # print("".join([secrets.choice(ul_case) for i in range(6)]))
    # print("".join([secrets.choice(ul_case)for i in range(2)])+"".join([secrets.choice(digits)for j in range(2)])+"".join([secrets.choice(ul_case)for i in range(2)]))
    print("".join([secrets.choice(string.ascii_uppercase)for i in range(5)])+"".join([secrets.choice(digits)for j in range(4)])+"".join([secrets.choice(string.ascii_uppercase)for i in range(1)]))
input()
