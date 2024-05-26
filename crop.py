
# Importing Image class from PIL module
from PIL import Image
import cv2
# Opens a image in RGB mode
im = Image.open(r"Image_data/218024572776_1.jpg")
img = cv2.imread(r"Image_data/218024572776_1.jpg")
dimension = img.shape
print(dimension)
 
# Setting the points for cropped image
left = 500
top = 665
right = 960
bottom = 970
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
print(type(im1))
#cv2.imwrite('croped.jpg',im1)
im1.save('image_cropped.jpg')
 
# Shows the image in image viewer
#im1.show()