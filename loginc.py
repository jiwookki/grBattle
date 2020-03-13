decrypted = b"abcdefghijklmnopqrstuvwxyz "
encrypted = b":;'@#$%^&*()_-=+!~`,./}{|5 "

encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)


def encrypt_password(message):
        global encrypt_table
        message = input('\nEnter message for encryption: ')
        result = message.translate(encrypt_table)
        return result


def decrypt_password(message):
        global decrypt_table
        result = message.translate(decrypt_table)
        return result

