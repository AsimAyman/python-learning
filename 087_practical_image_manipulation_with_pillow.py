# ---------------------------------------------------
# ------Practical => Image Manipulation with Pillow--
# ---------------------------------------------------

from PIL import Image

# open the image
myImage = Image.open(r'C:\Users\A\Desktop\sunset-1373171_640.webp')

# show the image
myImage.show()

# my crooped Image
myBox = (0,0,50,50)
newImage = myImage.crop(myBox)
newImage.show()

# my converted image mode
converted = myImage.convert("L")
converted.show()