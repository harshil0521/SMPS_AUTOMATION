import secrets
import string

ul_case = string.ascii_uppercase + string.ascii_lowercase
digits = string.digits
for k in range(5):
    print("".join([secrets.choice(ul_case)for i in range(7)])+"".join([secrets.choice(digits)for j in range(3)])+"".join([secrets.choice(ul_case)for i in range(5)]))
input()
