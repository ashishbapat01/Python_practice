

# Imports PIL module
from PIL import Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

drawing = svg2rlg("C:\Users\91860\PycharmProjects\pythonProject\myqr.svg")
renderPM.drawToFile(drawing, "file.png", fmt="PNG")

# open method used to open different extension image file
#im = Image.open(r"C:\Users\91860\PycharmProjects\pythonProject\myqr.svg")


# This method will show image in any image viewer
#im.show()
