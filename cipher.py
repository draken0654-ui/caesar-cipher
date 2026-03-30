def decrypt_incremental_shift(ciphertext):
    decrypted = ""
    for i, char in enumerate(ciphertext):
        # Subtract the position index (0-based) from the ASCII value
        original_char = chr(ord(char) - i)
        decrypted += original_char
    return decrypted

# Decrypt the given text
ciphertext = str(input("enter s"))
original_text = decrypt_incremental_shift(ciphertext)
print("Original text:", original_text)   