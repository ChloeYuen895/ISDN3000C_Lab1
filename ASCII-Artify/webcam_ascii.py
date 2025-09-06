import cv2
from PIL import Image
import numpy as np
import argparse
from rich.console import Console
from rich.text import Text

def map_pixel_to_char(pixel_value):
    ramp = map_pixel_to_char.ramp
    n_chars = len(ramp)
    index = int(pixel_value / 255 * (n_chars - 1))
    return ramp[index]

def frame_to_ascii(frame, width_chars, ascii_ramp):
    # Convert OpenCV BGR frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_frame)
    map_pixel_to_char.ramp = ascii_ramp

    # Resize image for color mode (keep RGBA if present)
    if pil_image.mode not in ("RGB", "RGBA"):
        color_image = pil_image.convert("RGBA")
    else:
        color_image = pil_image.copy()
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
    lines = []
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
        lines.append(line)
    return lines

def main():
    parser = argparse.ArgumentParser(description="Webcam to colored ASCII art in terminal.")
    parser.add_argument('--width', type=int, default=100, help='Width of ASCII art in characters (default: 100)')
    parser.add_argument('--ramp', type=str, default=".:-=+*#%@", help='ASCII character ramp from light to dark (default: ".:-=+*#%@")')
    args = parser.parse_args()

    width_chars = args.width
    ascii_ramp = args.ramp

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open webcam")
        return

    console = Console()
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break
            lines = frame_to_ascii(frame, width_chars, ascii_ramp)
            console.clear()
            for line in lines:
                console.print(line, end="\n")
            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()