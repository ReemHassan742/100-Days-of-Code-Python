import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  
symbols = ['!', '#', '$','%', '&', '(', ')', '-','+']

print("Welcome to the PyPassword Gererator")
nr_letters = int(input("How many letters would you like in your password"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))

# Esay Level 

password = ""

'''for i in range(0, nr_letters + 1):
    password += random.choice(letters)

for i in range(0, nr_symbols + 1):
    password += random.choice(symbols)

for i in range(0,nr_numbers + 1):
    password += random.choice(numbers)
    
print(password)
'''

# Hard level 

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
    
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
    
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
    
print(password_list)
random.shuffle(password_list)
print(password_list)

password= ""
for char in password_list:
    password += char
    
print(f"Your password is: {password}")