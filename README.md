🔐 Incremental Shift Cipher Decryption

This project provides a simple Python script to decrypt text encoded using an incremental shift cipher. In this cipher, each character in the plaintext is shifted forward based on its position index. The script reverses that process to recover the original message.

📌 How It Works
Each character in the ciphertext has been shifted by its index position.
The first character (index 0) is unchanged.
The second character (index 1) is shifted by +1, the third by +2, and so on.
To decrypt, the script subtracts the index from each character’s ASCII value.
🧠 Logic

For each character in the ciphertext:

original_char = chr(ord(char) - index)
💻 Code
def decrypt_incremental_shift(ciphertext):
    decrypted = ""
    for i, char in enumerate(ciphertext):
        # Subtract the position index (0-based) from the ASCII value
        original_char = chr(ord(char) - i)
        decrypted += original_char
    return decrypted

# Decrypt the given text
ciphertext = str(input("enter "))
original_text = decrypt_incremental_shift(ciphertext)
print("Original text:", original_text)
🚀 Usage

Clone the repository:

git clone https://github.com/your-username/incremental-shift-decryption.git

Navigate to the project folder:

cd incremental-shift-decryption

Run the script:

python script.py
Enter the encrypted text when prompted.
🧪 Example

Input:

ifmmp

Output:

hello
⚠️ Notes
This script assumes ASCII-based characters.
It may produce unexpected results for non-standard or Unicode characters.
No validation is included for malformed input.
📄 License

This project is open-source and available under the MIT License.
