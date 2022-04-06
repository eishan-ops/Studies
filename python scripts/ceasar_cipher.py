
Algorithm for generating ceasar ciper: 
--------------------------------------------------------------------------------------------------------------------------------------
This is as per my understanding till now : 

you have a a list of alphabets: 

store the input of the user as a string and also the 'Shift number' in a separate Var

create an empty list same as the length of the string entered by the user :

for every letter in the string - find that index of that letter in the list - 'alphabets' and add the value of 'shift number' to it.
	store this value in the empty list created above
	
now you have a list full of shifter index numbers.

for every shifted index numbers in the list : find that alphabet in the list 'alphabet' 
	put it in a new list or replace the index with the shifted alphabet (recommended: you a new list - -easy for debugging.)
	
Now you have the encrypted/shifted string.
--------------------------------------------------------------------------------------------------------------------------------------
#lists we use 
alphabets = []
shifted_indices = []
encrypted_string = []

#variable Declaration
text_to_encrypt = input("What text would you like to encrypt?\n").lower()
shift_number = int(input("What is the shift number?\n"))



for letter in text_to_encrypt:
	shifted_index = text_to_encrypt.index("letter") + shift_number
	shifted_indices.append(shifted_index)


for i in shifted_indices:
	encrypted_index.append(alphabets[i])
	
--------------------------------------------------------------------------------------------------------------------------------------

Things learnt from watching the lecture: 
	oBVIOSULY there are many way of implementing this
	Notice that you use 2 for loops : the problem can be solved using one for loop, this also means --\n
	that you might not even have to make use of 'shifted_indices' variable used to store a list
	ANOTHER THING: You dont need to convert everything to a LIST ! - also try working with strings: they are very similar, \n
	Instead of appending values to a list you can just use string concatenation. 
	appending to list also adds the over head of eventually convverting it back to a string to display it ! ** remember this.
	
	Conclusion : Minimize variable creation .
				Minimize number of for loops.
				Working with strings INSTEAD of lists wherever possible.
				



	
