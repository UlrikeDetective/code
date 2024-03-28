from PIL import Image, ImageDraw, ImageFont

def diamond_shape_to_image(msg="I like kindness"):
    lines = []

    for y in range(10):
        line = " " * (10 - y) + "*" * (2 * y + 1)
        lines.append(line)

    for y in range(9, -1, -1):
        line = " " * (10 - y) + "*" * (2 * y + 1)
        lines.append(line)

    # Calculate the width and height for the image
    width = len(lines[0]) * 8
    height = len(lines) * 15

    # Additional height for the message
    message_height = 50

    # Create a new image with a white background
    total_height = height + message_height
    img = Image.new('RGB', (width, total_height), color='black')
    draw = ImageDraw.Draw(img)
    
    # Use a monospace font for better alignment
    font = ImageFont.load_default()

    # Draw the diamond shape
    y_offset = 0
    for line in lines:
        draw.text((0, y_offset), line, fill='yellow', font=font)
        y_offset += 15

    # Draw the message at the bottom
    draw.text((10, height), msg, fill='white', font=font)

    # Save the image as a PNG file
    img.save('diamond.png')

# Call the function to create the diamond shape with a message and save it as an image
diamond_shape_to_image()


from PIL import Image, ImageDraw, ImageFont

def smiley_face_to_image():
    lines = [
        "       *****       ",
        "     *       *     ",
        "   *           *   ",
        " *               * ",
        " *   *********   * ",
        " *   *       *   * ",
        "   *           *   ",
        "     *********     "
    ]

    width = len(lines[0]) * 10
    height = len(lines) * 15

    img = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    y_offset = 0
    for line in lines:
        draw.text((0, y_offset), line, fill='yellow', font=font)
        y_offset += 15

    img.save('smiley.png')

# Call the function to create a smiley face and save it as an image
smiley_face_to_image()


from PIL import Image, ImageDraw, ImageFont

def star_shape_to_image(msg="great work"):
    lines = [
        "        *        ",
        "      *   *      ",
        "    *       *    ",
        "  *           *  ",
        "***************",
        "  *   GREAT   *  ",
        "  *    WORK   *  ",
        "  *           *  ",
        "    *       *    ",
        "      *   *      ",
        "        *        "
    ]

    width = len(lines[0]) * 8
    height = len(lines) * 15

    img = Image.new('RGB', (width, height), color='red')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    y_offset = 0
    for line in lines:
        draw.text((0, y_offset), line, fill='white', font=font)
        y_offset += 15

    img.save('star.png')

# Call the function to create the star shape with the message and save it as an image
star_shape_to_image()

#EasterEgg_mess

from colorama import Fore
from PIL import Image, ImageDraw, ImageFont

def egg_shape_to_image(msg="Happy Easter!", font_size=20):
    lines = [
        "       * * * * *",
        "     *             *",
        "   *                 *",
        "  *                    *",
        "**************",
        " *   Happy             *",
        " *   Easter!          *",
        "  *                  *",
        "    *              *",
        "      *          * ",
        "        *** * *"
    ]

    width = len(lines[0]) * 8
    height = len(lines) * 15

    img = Image.new('RGB', (width, height), color='green')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    y_offset = 0
    for line in lines:
        draw.text((0, y_offset), line, fill='yellow', font=font)
        y_offset += 15

    img.save('easter_egg.png')

# Call the function to create the star shape with the message and save it as an image
egg_shape_to_image()
