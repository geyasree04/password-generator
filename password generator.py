import random
import string

sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

letter = int(input("How many letters do you want in your password? "))
sp_sym = int(input("How many symbols do you want? "))
num = int(input("How many numbers do you want in your password? "))

password = []

for i in range(letter):
    password.append(random.choice(string.ascii_letters))  # picks a random letter

for i in range(sp_sym):
    password.append(random.choice(sym))  # picks a random symbol

for i in range(num):
    password.append(str(random.randint(0, 9)))  # picks a random digit

random.shuffle(password)  # shuffles the whole list

print("Your password:", ''.join(password))