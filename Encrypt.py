
class Encryptor:

    def __init__(self):
        self.key = 20

    def encrypt(self, text):
        encrypted_text = ''

        for symb in text:
            encrypted_text += chr(ord(symb) + self.key)

        return encrypted_text

    def decrypt(self, text):
        decrypt_text = ''

        for symb in text:
            decrypt_text += chr(ord(symb) - self.key)

        return decrypt_text


enc = Encryptor()
enc.encrypt('hello')
