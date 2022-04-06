import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



password = []


for i in range(0, nr_letters):
	password.append(letters[random.randint(0 , len(letters) - 1 )])
	
for j in range(0, nr_symbols):
	insert_at = random.randint(0, len(password) - 1)
	password.insert(insert_at, letters[random.randint(0 , len(symbols) - 1 ])
	
for k in range(0, nr_numbers):
	insert_at = random.randint(0, len(password) - 1)
	password.insert(insert_at, letters[random.randint(0 , len(numbers) - 1 ])

password_as_string = ''.join(password)

print(f"your final password is {password_as_string}")





