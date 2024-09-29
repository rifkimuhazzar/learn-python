def vigenere_chiper(message, key, direction = 1):
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_text_message = ""

    for char in message.lower():
        if not char.isalpha():
            final_text_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            
            char_index = alphabet.index(char)
            offset = alphabet.index(key_char)
            new_key_index = (char_index + (offset * direction)) % len(alphabet)
            final_text_message += alphabet[new_key_index] 
        
    return final_text_message

def encrypt(message, key):
    return vigenere_chiper(message, key)

def decrypt(message, key):
    return vigenere_chiper(message, key, -1)

# Plain text to encrypt/decrypt text
text_message = "Hello This Is The Text Before Encrypted!"
custom_key = "gwehiobchivuqzalpgheroiuj"

encryption = encrypt(text_message, custom_key)
decryption = decrypt(encryption, custom_key)
print("\n--- Plain text to encrypt/decrypt text")
print(f"Encrypted Text: {encryption}")
print(f"Decrypted Text: {decryption}")

# From ecnrypt text to decrypt text
encrypt_text = "mrttaqrhknsw ih puggrur"
custom_key = "happycoding"

decryption = decrypt(encrypt_text, custom_key)
print("\n--- From ecnrypt text to decrypt text")
print(f"Decrypted Text: {decryption}")