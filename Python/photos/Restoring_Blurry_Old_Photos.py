# Restoring Blurry Old Photos 

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

# Load the image and convert it to grayscale
def load_image(image_path):
    img = Image.open(image_path)
    return img.convert("L")

# Denoise the image
def denoise_image(image, weight=0.1):
    img_array = np.asarray(image, dtype=np.float32)
    out_array = img_array.copy()
    out_array[1:-1, 1:-1] = img_array[1:-1, 1:-1] * (1 - 4 * weight) + \
                            (img_array[:-2, 1:-1] + img_array[2:, 1:-1] + img_array[1:-1, :-2] + img_array[1:-1, 2:]) * weight
    return Image.fromarray(np.uint8(out_array), "L")

# Sharpen the image
def sharpen_image(image, radius=2, percent=150):
    return image.filter(ImageFilter.UnsharpMask(radius=radius, percent=percent, threshold=3))

# Display the image
def display_image(image):
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.show()

# Main program
def main():
    image_path = "/Users/ulrike_imac_air/Library/Mobile Documents/com~apple~CloudDocs/Bilder/Lightroom/Familienfotos_vor_2009/vor_2009_London_Familienfotos_Lightroom-01.jpg"  # Replace with your image path

    # Load the image
    image = load_image(image_path)

    # Denoise the image
    denoised_image = denoise_image(image)

    # Sharpen the image
    sharpened_image = sharpen_image(denoised_image)

    # Display the original image
    print("Original Image:")
    display_image(image)

    # Display the processed image
    print("Processed Image:")
    display_image(sharpened_image)

if __name__ == "__main__":
    main()
