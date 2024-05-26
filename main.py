#**************** IMPORT PACKAGES ********************
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import warnings
warnings.filterwarnings("ignore")
import os

from model import File_Pass
from PIL import Image
import cv2

def crop_fun(file_path):
    # Opens a image in RGB mode
    im = Image.open("Image_data/"+file_path)
    #img = cv2.imread(r"Image_data/218024572776_1.jpg")
    #dimension = img.shape
    #print(dimension)
     
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

#***************** FLASK *****************************
app = Flask(__name__)

class main:
    def __init__(self):
        self.filename = "218024.jpg"

@app.route('/', methods=['GET'])
def about():
    return render_template('index.html')

@app.route('/Result', methods=['POST', 'GET'])
def result():
    f = request.files['file']
    iname = f.filename
    crop_fun(iname)  
    obj = File_Pass(iname)
    im_result= obj.get_text()
    return render_template('result.html', caption=im_result)

if __name__ == '__main__':
    app.run(debug=True)
