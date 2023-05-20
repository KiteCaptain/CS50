import os
import qrcode
import subprocess as sp

img = qrcode.make("https://github.com/Milton-Ngala/face_recognition/blob/master/examples/recognize_faces_in_pictures.py")
img.save("qr.png", "PNG")

# Open the QR code using the default system viewer
# if os.name == "nt": # windows
#     sp.run(["start", "qr.png"], shell=True)
# elif os.name == "posix": # macOs and Linux
#     sp.run(["xdg-open", "qr.png"])