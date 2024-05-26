# Install Dependencies
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd

class File_Pass:
    def __init__(self,name):
        self.name = name
    
    def get_text(self):
        # img = self.name
        # path = 'Image_data/'
        # location=path+img
        # print(location)
        # image = cv2.imread(path+img)
        image = cv2.imread('image_cropped.jpg')

        # 'en' is specifying English OCR 
        reader = easyocr.Reader(['en'])      
        result = reader.readtext(image)
        # Result shows the Coordinates, Text and Score
        #result

        # Text from an image
        text = [result[res][1] for res in range(len(result))]

        data =''
        for i in text:
            print(i)
            #print(type(i))
            data +=i
            data+= ' '
            print(data)
        

        return data