# Find faces in a picture
from PIL import Image
import  face_recognition as fr

# Load the jpg file into a numpy array
image = face_recognition.loadfile("big_bang.jpg")

# Find all the faces in the image using the default HOG-based model
#  See also: find_faces_in_picture_cnn.py - uses the  CNN model
face_locations = fr.face_locations(image)
for face in face_locations:
    # Print the location of each face in this image
    top, right, bottom, left = face_location
    
    # Accessing tha actual faces
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()    
    