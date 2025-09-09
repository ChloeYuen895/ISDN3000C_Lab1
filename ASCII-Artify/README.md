# ASCII-Artify


This project provides Python scripts to convert images and webcam video into ASCII art, with optional color output using the `rich` library. It also includes a script that uses OpenCV (`cv2`) to capture webcam video and generate ASCII art in real time, displaying the live ASCII output directly in your terminal.

## Requirements
Install dependencies from `requirements.txt`:
  ```sh
  pip install -r requirements.txt
  ```

## Scripts

### 1. `main.py`
Converts an image to ASCII art and prints it in the terminal (monochrome, no color).

**Usage:**
```sh
python main.py <image_path> [--width WIDTH] [--ramp RAMP]
```
- `<image_path>`: Path to the image file (JPG, PNG, etc.)
- `--width`: Width of ASCII art in characters (default: 100)
- `--ramp`: ASCII character ramp from light to dark (default: .:-=+*#%@)

**Example:**
```sh
python main.py assets/mimikyu.png --width 80 --ramp ".:-=+*#%@"
```

---

### 2. `ascii_color.py`
Converts an image to colored ASCII art using the `rich` library. Handles transparency in PNGs by printing spaces.

**Usage:**
```sh
python ascii_color.py <image_path> [--width WIDTH] [--ramp RAMP]
```
- `<image_path>`: Path to the image file (JPG, PNG, etc.)
- `--width`: Width of ASCII art in characters (default: 100)
- `--ramp`: ASCII character ramp from light to dark (default: .:-=+*#%@)

**Example:**
```sh
python ascii_color.py assets/mimikyu.png --width 50 --ramp "018"
```

---

### 3. `webcam_ascii.py`
Captures webcam video and displays it as live colored ASCII art in the terminal using the `rich` library.

**Usage:**
```sh
python webcam_ascii.py [--width WIDTH] [--ramp RAMP]
```
- `--width`: Width of ASCII art in characters (default: 100)
- `--ramp`: ASCII character ramp from light to dark (default: .:-=+*#%@)

**Example:**
```sh
python webcam_ascii.py --width 80 --ramp ".:-=+*#%@"
```

Press `q` in the terminal window to quit the webcam stream.

---

## Notes
- For best results, use images with good contrast.
- PNGs with transparency will show transparent areas as spaces in colored ASCII output.
- The `rich` library is required for colored output.
