# main.py
import os
from image_cipher import encrypt_image, decrypt_image

def clear_screen():
    # Optional: clear terminal for nicer output
    os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        print("=" * 50)
        print(" Pixel Manipulation Image Encryption Tool ")
        print("=" * 50)
        print("1. Encrypt image")
        print("2. Decrypt image")
        print("3. Exit")
        print("=" * 50)

        choice = input("Choose an option (1-3): ").strip()

        if choice == "3":
            print("Exiting...")
            break

        if choice not in ("1", "2"):
            print("Invalid choice, please try again.\n")
            continue

        input_path = input("Enter input image path (e.g. sample.png): ").strip()
        if not os.path.exists(input_path):
            print("File not found, please check the path.\n")
            continue

        key_str = input("Enter numeric key (e.g. 123): ").strip()
        if not key_str.isdigit():
            print("Key must be a positive integer.\n")
            continue

        key = int(key_str)

        if choice == "1":
            output_path = input(
                "Enter output encrypted image name (e.g. encrypted.png): "
            ).strip()
            encrypt_image(input_path, output_path, key)
            print(f"Image encrypted and saved as: {output_path}\n")

        elif choice == "2":
            output_path = input(
                "Enter output decrypted image name (e.g. decrypted.png): "
            ).strip()
            decrypt_image(input_path, output_path, key)
            print(f"Image decrypted and saved as: {output_path}\n")


if __name__ == "__main__":
    clear_screen()
    main()
