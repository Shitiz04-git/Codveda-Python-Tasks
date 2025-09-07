# caesar_cipher_file.py

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt only letters
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep other characters unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def process_file(file_path, shift, mode):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        
        if mode == "encrypt":
            result = encrypt(content, shift)
            new_file = file_path.replace(".txt", "_encrypted.txt")
        elif mode == "decrypt":
            result = decrypt(content, shift)
            new_file = file_path.replace(".txt", "_decrypted.txt")
        else:
            print("Invalid mode!")
            return
        
        with open(new_file, "w") as file:
            file.write(result)
        
        print(f"File processed successfully! New file: {new_file}")
    
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

def main():
    print("----- Caesar Cipher File Encryption/Decryption -----")
    file_path = input("Enter file path (e.g., sample.txt): ")
    shift = int(input("Enter shift value (e.g., 3): "))
    mode = input("Enter mode (encrypt/decrypt): ").lower()

    process_file(file_path, shift, mode)

if __name__ == "__main__":
    main()
