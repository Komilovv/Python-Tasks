# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:13:27 2023

@author: ADMIN
"""

import numpy as np
from PIL import Image
import cv2

# Open the main image and the image to insert
main_image = Image.open("C:/Onam/task.jpg")
insert_image = Image.open("C:/Onam/o`zim.jpg")

# Define the corresponding points for the board
main_points = np.array([[195, 106], [693, 243], [193, 575], [692, 485]], dtype=float)  # Main image points
insert_points = np.array([[0, 0], [719, 0], [0, 1278], [719, 1278]], dtype=float)  # Insert image points

# Calculate the perspective transformation matrix
matrix, _ = cv2.findHomography(insert_points, main_points)

# Apply the perspective transformation to the insert image
insert_image = cv2.warpPerspective(np.array(insert_image), matrix, (main_image.width, main_image.height))

# Create a mask as a binary image
mask_data = cv2.warpPerspective(np.ones((main_image.height, main_image.width), np.uint8), matrix, (main_image.width, main_image.height))

# Convert the mask to a grayscale image
mask_image = Image.fromarray(mask_data * 255, 'L')

# Paste the transformed insert image onto the main image using the mask
main_image.paste(Image.fromarray(insert_image), (0, 0), mask_image)

# Display or save the final image
main_image.show()
