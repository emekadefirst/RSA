from main import Scheme

def alphabet_to_number(alphabet):
    return ord(alphabet.lower()) - 96 if alphabet.isalpha() else None

def number_to_alphabet(number):
    if number == 0:  # Representing space
        return ' '  # Return space
    elif 1 <= number <= 26:
        return chr(number + 96)  # For letters
    else:
        return "Not a valid number."

response = str(input("What would you like to do\n1. Encrypt data\n2. Decrypt data\n>> "))
public_key = int(input("Enter Your Public-key\n>> "))
secret_key = int(input("Enter Your Secret-key\n>> "))

if response == "1":
    message = str(input("Enter Your message\n>> ")).strip()
    data = [alphabet_to_number(char) for char in message if alphabet_to_number(char) is not None]
    message_obj = Scheme(secret_key, public_key, data)
    encrypted_data = message_obj.encrypt()
    encrypted_string = ''.join(str(digit) for digit in encrypted_data)
    print("Encrypted data:", encrypted_string)
elif response == "2":
    message = str(input("Enter Your message\n>> ")).strip()
    data = [int(digit) for digit in message if digit.isdigit()]
    message_obj = Scheme(secret_key, public_key, data)
    
    # Decrypting the encrypted message
    decrypted_data = message_obj.decrypt(data)
    decrypted_string = ''.join(number_to_alphabet(digit) if digit is not None else '' for digit in decrypted_data)
    print("Decrypted data:", decrypted_string)
else:
    print("Invalid option. Please select either '1' or '2'.")
