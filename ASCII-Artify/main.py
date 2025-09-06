import sys
import argparse
from PIL import Image

# Default character ramp
DEFAULT_ASCII_CHARS = ".:-=+*#%@"

def resize_and_grayscale(image, new_width=100):
    # Resize image to new_width, maintain aspect ratio
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    # Convert to grayscale
    grayscale_image = resized_image.convert("L")
    return grayscale_image

def map_pixel_to_char(pixel_value):
    # Map pixel value (0-255) to a character in the current ramp
    ramp = map_pixel_to_char.ramp
    n_chars = len(ramp)
    index = int(pixel_value / 255 * (n_chars - 1))
    return ramp[index]

def main():
    parser = argparse.ArgumentParser(description="Convert images to ASCII art.")
    parser.add_argument('image_path', help='Path to the image file')
    parser.add_argument('--width', type=int, default=100, help='Width of ASCII art in characters (default: 100)')
    parser.add_argument('--ramp', type=str, default=DEFAULT_ASCII_CHARS, help='ASCII character ramp from light to dark (default: ".:-=+*#%@")')
    args = parser.parse_args()

    image_path = args.image_path
    width_chars = args.width
    ascii_ramp = args.ramp

    # Set the ramp for the mapping function
    map_pixel_to_char.ramp = ascii_ramp

    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: File not found at '{image_path}'")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    # 1. Resize and convert the image
    ascii_image = resize_and_grayscale(image, new_width=width_chars)

    # 2. Get the pixel data
    pixels = ascii_image.getdata()
    width, height = ascii_image.size

    # 3. Build the ASCII string
    ascii_str = ""
    for i, pixel in enumerate(pixels):
        ascii_str += map_pixel_to_char(pixel)
        # Newline at the end of each row
        if (i + 1) % width == 0:
            ascii_str += "\n"

    # 4. Print the final art
    print(ascii_str)


if __name__ == "__main__":
    main()