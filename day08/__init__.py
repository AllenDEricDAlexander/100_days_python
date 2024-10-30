# Day 8 - Beginner - Function Parameters & Caesar Cipher

# function with inputs

def greet(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet("James", "London")


# Caesar Cipher

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetical characters remain unchanged
            result += char

    return result


# 示例用法
if __name__ == "__main__":
    original_text = "Hello, World!"
    shift_value = 3

    encrypted_text = caesar_cipher(original_text, shift_value, mode='encrypt')
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = caesar_cipher(encrypted_text, shift_value, mode='decrypt')
    print(f"Decrypted: {decrypted_text}")
