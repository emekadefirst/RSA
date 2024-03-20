
class Scheme:
    def __init__(self, secret_key, public_key, message):
        self.public_key = public_key
        self.secret_key = secret_key
        self.message = message
        
    def encrypt(self):
        encrypted_message = [(char**self.public_key)%self.secret_key for char in self.message]
        return encrypted_message
    
    def decrypt(self, encrypted_message):
        decrypted_message = [char**self.secret_key%self.public_key for char in encrypted_message]
        return decrypted_message
