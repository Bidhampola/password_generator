### week 1 project... password generator

import string
import random

print("Welcome to password generator! ")

#input the length of the password
length=int(input('\n Enter the length of the password: '))

#defining data
num=string.digits
lower=string.ascii_lowercase
upper=string.ascii_uppercase
symbols=string.punctuation

#combining all data
all = upper+upper + lower+lower + num+num + symbols+symbols

#using random

temp=random.sample(all,length)

#creating a password
password = "".join(temp)

# output password
print(password)
