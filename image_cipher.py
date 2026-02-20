# image_cipher.py
from PIL import Image  # pip install pillow

def _process_image(input_path: str, output_path: str, key: int) -> None:
    """
    Encrypt or decrypt an image using XOR on each RGB value.
    Using XOR makes encryption and decryption the same operation.
    """
    img = Image.open(input_path).convert("RGB")
    width, height = img.size
    pixels = img.load()

    key = key % 256  # keep key in 0–255

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r_new = r ^ key
            g_new = g ^ key
            b_new = b ^ key
            pixels[x, y] = (r_new, g_new, b_new)

    img.save(output_path)


def encrypt_image(input_path: str, output_path: str, key: int) -> None:
    _process_image(input_path, output_path, key)


def decrypt_image(input_path: str, output_path: str, key: int) -> None:
    _process_image(input_path, output_path, key)
