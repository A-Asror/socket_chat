import settings


class Encryptor:

    def encrypt(self, text):
        encrypted_text = ''

        for symb in text:
            encrypted_text += chr(ord(symb) + settings.ENCRYPTION_KEY)

        return encrypted_text

    def decrypt(self, text):
        decrypt_text = ''

        for symb in text:
            decrypt_text += chr(ord(symb) - settings.ENCRYPTION_KEY)

        return decrypt_text


enc = Encryptor()
enc.encrypt('hello')
