from colorama import Fore, Back, Style, init
init(autoreset=True)
from PIL import Image
import pyfiglet

ASCII_CHARS = "@%#*+=-:. "
def image_to_ascii(image_path, new_width=200):
    img = Image.open(image_path).convert("L")

    # Adjust size
    width, height = img.size
    new_height = int((height / width) * new_width * 0.5)
    img = img.resize((new_width, new_height))

    # Transform pixels to ASCII chars
    pixels = img.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // 32] for pixel in pixels)

    # Format into lines
    ascii_lines = [
        ascii_str[i: i + new_width] for i in range(0, len(ascii_str), new_width)
    ]

    # Find positions of ":"
    positions = []
    for y, line in enumerate(ascii_lines):
        for x, char in enumerate(line):
            if char == ":":
                positions.append((x, y))  # Store (x, y) positions

    return ascii_lines, positions


def insert_char_at_positions(ascii_lines, positions, char="´"):
    """Replace characters at specified positions in the ASCII lines."""
    ascii_list = [list(line) for line in ascii_lines]  # Convert to list of lists (mutable)

    for x, y in positions:
        ascii_list[y][x] = char  # Replace character

    return "\n".join("".join(line) for line in ascii_list)  # Convert back to string

def replace_at_index(original: str, replacement: str, index: int):
    return original[:index] + replacement + original[index + len(replacement):]

# Example usage:
if __name__ == "__main__":
    ascii_art, positions = image_to_ascii("services/articleus.png", new_width=76)
    team_names = ["Richard", "Paula", "Dennis", "Sonam", "Hasnain"]
    for i in range(4,9):
        ascii_art[i] = replace_at_index(ascii_art[i], team_names[i-4], 40)

    print(Fore.BLUE + "\n".join(ascii_art))  # Print original ASCII

