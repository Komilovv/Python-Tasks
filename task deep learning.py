# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:58:28 2023

@author: ADMIN
"""

from PIL import Image

# Open the main image where you want to insert the second image
main_image = Image.open("C:/Onam/uy.jpg")

# Open the image you want to insert (in this case, "o`zim.jpg")
insert_image = Image.open("C:/Onam/o`zim.jpg")

# Create a blank canvas with the same size as the main image
canvas = Image.new("RGB", main_image.size)

# Paste the main image onto the canvas
canvas.paste(main_image, (0, 0))

# Calculate the position where you want to insert the second image
# For example, let's insert it at coordinates (100, 100)
position = (500, 500)

# Paste the second image onto the canvas at the specified position
canvas.paste(insert_image, position)

# Save the final image to a file
canvas.save("C:/Onam/output_image.jpg")

# Display the final image
canvas.show()


