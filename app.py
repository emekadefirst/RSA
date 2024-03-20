from main import Scheme

public_key = int(input("Enter Your Public-key\n>> "))
secret_key = int(input("Enter Your Secret-key\n>> "))
message = str(input("Enter Your message\n>> ")).strip()

def alphabet_to_number(alphabet):
    return ord(alphabet.lower()) - 96 if alphabet.isalpha() else None

# Convert message to numbers
data = [alphabet_to_number(char) for char in message if alphabet_to_number(char) is not None]

# Encrypting the message
message_obj = Scheme(secret_key, public_key, data)
encrypted_data = message_obj.encrypt()
encrypted_string = ''.join(str(digit) for digit in encrypted_data)

print("Encrypted data:", encrypted_string)

# # Decrypting the encrypted message
# decrypted = message_obj.decrypt(encrypted_data)
# decrypted_string = ''.join(str(digit) for digit in decrypted)

# print("Decrypted data:", decrypted_string)
