# Identigy and draw box on a recognized face

import face_recognition as fr
import numpy as np
from PIL import Image, ImageDraw

# Load a sample picture and learn how to recognize it
known_image = fr.load_image_file("sheldon.jpg")
encoding = fr.face_encodings(known_image)[0]

# Load an image with know faces 
unknown_image = fr.load_image_file("big_bang.jpg")

# Find all faces and face_encodings in the known image
face_locations = fr.face_locations(unknown_image)
face_encoding = fr.face_encodings(unknown_image, face_locations)

# Convert the image to PIL format to draw marker
pil_image = Image.fromarray(unknown_image)

# Create a pillow ImageDraw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found int the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, ):
    pass

    