import sys
import argparse
from PIL import Image
from rich.console import Console
from rich.text import Text

def map_pixel_to_char(pixel_value):
    ramp = map_pixel_to_char.ramp
    n_chars = len(ramp)
    index = int(pixel_value / 255 * (n_chars - 1))
    return ramp[index]

def main():
    parser = argparse.ArgumentParser(description="Convert images to colored ASCII art.")
    parser.add_argument('image_path', help='Path to the image file')
    parser.add_argument('--width', type=int, default=100, help='Width of ASCII art in characters (default: 100)')
    parser.add_argument('--ramp', type=str, default=".:-=+*#%@", help='ASCII character ramp from light to dark (default: ".:-=+*#%@")')
    args = parser.parse_args()

    image_path = args.image_path
    width_chars = args.width
    ascii_ramp = args.ramp
    map_pixel_to_char.ramp = ascii_ramp

    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: File not found at '{image_path}'")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    # Resize image for color mode (keep RGBA if present)
    if image.mode not in ("RGB", "RGBA"):
        color_image = image.convert("RGBA")
    else:
        color_image = image.copy()
    width_orig, height_orig = color_image.size
    aspect_ratio = height_orig / width_orig
    new_height = int(width_chars * aspect_ratio)
    color_image = color_image.resize((width_chars, new_height))

    # Grayscale for ASCII mapping
    ascii_image = color_image.convert("L")
    ascii_pixels = list(ascii_image.getdata())
    color_pixels = list(color_image.getdata())
    width, height = ascii_image.size

    console = Console()
    for y in range(height):
        line = Text()
        for x in range(width):
            idx = y * width + x
            gray = ascii_pixels[idx]
            char = map_pixel_to_char(gray)
            color = color_pixels[idx]
            # Handle transparency: if alpha==0, print space
            if isinstance(color, tuple) and len(color) == 4 and color[3] == 0:
                line.append(" ")
            else:
                if isinstance(color, tuple):
                    r, g, b = color[:3]
                else:
                    r = g = b = color
                line.append(char, style=f"rgb({r},{g},{b})")
        console.print(line, end="\n")

if __name__ == "__main__":
    main()
