class Scheme:
    def __init__(self, secret_key, public_key, message):
        self.public_key = public_key
        self.secret_key = secret_key
        self.message = message
        
    def encrypt(self):
        encrypted_message = (self.message**self.public_key)%self.secret_key
        return encrypted_message
    
    def decrypt(self, encrypted_message):
        decrypted_message = (encrypted_message**self.secret_key)%self.public_key
        return decrypted_message  


# Encrypting the message
message = Scheme(5, 14, 2)  # Here, the public_key is 5 and the secret_key is 14
encrypted_data = message.encrypt()
print("Encrypted data:", encrypted_data)

# Decrypting the encrypted message
decrypted = message.decrypt(encrypted_data)
print("Decrypted data:", decrypted)
