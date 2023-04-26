from fastapi import File, UploadFile,HTTPException, status
from fastapi.responses import FileResponse
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
import os,csv
import shutil
import requests
import pathlib
from typing import List
from datetime import datetime

ImageLocation="C:\\Sonam\\Project\\Kas Project\\app\images\\"
input_shape= (224, 224)

def load_model():
        model = tf.keras.applications.MobileNetV2(weights="imagenet")
        print("Model loaded")
        return model
model = load_model()

class imageRepository():
    def add_user(user):
        with open('data/users.json', 'w')as f:
            f.write(str(imageRepository))
            
    def read_imagefile(file) -> Image.Image:
        image = Image.open(BytesIO(file))
        return image

    def UploadSingleImage(image: UploadFile = File(...)):
        file_extension = pathlib.Path(str(image.filename)).suffix
        uplodedFileName="CropImage"+ str(datetime.now().strftime('%Y-%m-%d %H-%M-%S')) + file_extension
       
        with open(ImageLocation+uplodedFileName, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        return {"filename": uplodedFileName +str(image)}
    
    
    def UploadPredictImage(image: UploadFile = File(...)):

        MaxImageSizeinMB=2        
         # Get the file size (in bytes)
        image.file.seek(0, 2)
        file_size = image.file.tell()

        # move the cursor back to the beginning
        image.seek(0)

        if file_size > MaxImageSizeinMB * 1024 * 1024:
        # more than 2 MB
         raise HTTPException(status_code=400, detail="File is too large. Max allowed size is :"+ str(MaxImageSizeinMB) +"MB")
        
        # check the content type (MIME type)
        content_type = image.content_type
        if content_type not in ["image/jpeg", "image/png", "image/gif", "image/svg+xml"]:
         raise HTTPException(status_code=400, detail="Invalid file type. Please upload image of file type: Jpeg,png,gif,jpg,bmp ")

        #Save File
        file_extension = pathlib.Path(str(image.filename)).suffix
        uplodedFileName="CropImage"+ str(datetime.now().strftime('%Y-%m-%d %H-%M-%S')) + file_extension
        fileSize=0
        with open(ImageLocation+uplodedFileName, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        #return response
        return {"Image uploded sucessfully. File Name:" + uplodedFileName +" , File Size:"+ str(file_size) +" Byte, File Type:" + content_type}
    



    def UplodeMultiImage(file:List[UploadFile] = File(...)):
        file_extension = pathlib.Path(str(file.filename)).suffix
        uplodedFileName="CropImage"+ str(datetime.now().strftime('%Y-%m-%d %H-%M-%S')) + file_extension
            
        with open(ImageLocation+uplodedFileName, "wb") as buffer:
            shutil.copyfileobj(Image.files, buffer)
    
        return { "filenames": "file sucessfully uploded"}

    

    



    






