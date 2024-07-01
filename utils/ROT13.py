def decrypt_rot13(text):
    decrypted_text = []
    
    for char in text:
        if 'A' <= char <= 'Z':  # Caracter es una letra mayúscula
            decrypted_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':  # Caracter es una letra minúscula
            decrypted_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            decrypted_char = char  # Mantener caracteres que no son letras
            
        decrypted_text.append(decrypted_char)
    
    return ''.join(decrypted_text)

# Ejemplo de uso:
encrypted_message = str(input("Introduce un mensaje encriptado con ROT13: "))
decrypted_message = decrypt_rot13(encrypted_message)

print("Mensaje encriptado:", encrypted_message)
print("Mensaje desencriptado:", decrypted_message)
