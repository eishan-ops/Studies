def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)

---------------------------------------------------------------------------
---------------------------------------------------------------------------

#NEWLY Written code for the Ceaser Cipher:


print("Welcome to Ceasar cipher!!")
wish = lower(input("Do you wish to encode or decode?\n"))

text = input("Enter you text-\n")
shift = input("Enter your shift amount-\n")
if shift > 26:
	shift %= 26




def encrypt(plain_text, shift_amount):
	cipher_text = ""
	for letter in plain_text:
		position = alphabet.index(letter)
		new_position = position + shift_amount
		cipher_text += alphabet[new_position]
		
def decrypt(cipher_text, shift_amount):
	plain_text = ""
	for letter in cipher_text:
		position = alphabet.index(letter)
		new_position = position - shift_amount
		plain_text += alphabet[new_position]
		
		
		
if wish == "encode":
	encrypt(plain_text = text, shift_amount = shift)
elif wish == "decode":
	decrypt(cipher_text = text, shift_amount = shift)
else:
	print("Please enter a valid text..")
	












