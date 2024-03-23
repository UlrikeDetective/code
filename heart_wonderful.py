from colorama import Fore
from PIL import Image, ImageDraw, ImageFont

def heart_shape_to_image(msg="wonderful"):
    lines = []

    for y in range(15, -15, -1):
        line = ""
        for x in range(-30, 30):
            f = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            line += msg[(x - y) % len(msg)] if f <= 0 else " "
        lines.append(line)

    # Calculate the width and height for the image
    width = len(lines[0]) * 8
    height = len(lines) * 15

    # Create a new image with a white background
    img = Image.new('RGB', (width, height), color='lightblue')
    draw = ImageDraw.Draw(img)
    
    # Use a monospace font for better alignment
    font = ImageFont.load_default()

    # Draw the text on the image
    y_offset = 0
    for line in lines:
        draw.text((0, y_offset), line, fill='green', font=font)
        y_offset += 15

    # Save the image as a PNG file
    img.save('heart_wonderful.png')

# Call the function to create the heart and save it as an image
heart_shape_to_image()
