class Scheme:
    def __init__(self, secret_key, public_key, message):
        self.public_key = public_key
        self.secret_key = secret_key
        self.message = message
        
    def encrypt(self):
        a = self.secret_key**self.message
        encrypted_message = a%self.public_key
        return encrypted_message
    
    def decrypt(self):
        decrypted_message = (self.secret_key**self.message)%self.public_key
        return decrypted_message  


# Encrypting the message
message = Scheme(11, 14, 2)  # Here, the public_key is 11 and the secret_key is 14
encrypted_data = message.encrypt()
print(encrypted_data)

# Decrypting the encrypted message
decrypted = Scheme(11, 14, encrypted_data)  # Here, the public_key is 11 and the secret_key is 14
print(decrypted.decrypt())

# # Convert decrypted value to alphabet
# decrypted_alphabet = chr(decrypted_value + 95) if decrypted_value > 0 else 'a'
# print(decrypted_alphabet)
