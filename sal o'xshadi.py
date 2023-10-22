# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:42:13 2023

@author: ADMIN
"""
import numpy as np
from PIL import Image
import cv2  # Add this import for OpenCV

# Rest of your code remains the sam

# Open the main image and the image to insert
main_image = Image.open("C:/Onam/task.jpg")
insert_image = Image.open("C:/Onam/o`zim.jpg")

# Define the corresponding points
main_points = np.array([[195, 106], [693, 243], [193, 575], [692,485 ]], dtype=float)  # Main image points
insert_points = np.array([[0, 0], [719, 0], [0, 1238], [719, 1238]], dtype=float)  # Insert image points

# Calculate the perspective transformation matrix
matrix, _ = cv2.findHomography( insert_points,main_points)

# Apply the perspective transformation to the insert image
insert_image = cv2.warpPerspective(np.array(insert_image), matrix, (main_image.width, main_image.height))

# Paste the transformed insert image onto the main image
main_image.paste(Image.fromarray(insert_image), (0, 0))

# Display or save the final image
main_image.show()
