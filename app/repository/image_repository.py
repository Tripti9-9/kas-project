from fastapi import File, UploadFile,HTTPException, status
from fastapi.responses import FileResponse
import os,csv
import shutil
import requests
import pathlib
from typing import List
from datetime import datetime

ImageLocation="C:\\Sonam\\Project\\Kas Project\\app\images\\"

class imageRepository():
    def add_user(user):
        with open('data/users.json', 'w')as f:
            f.write(str(imageRepository))

    def UploadSingleImage(image: UploadFile = File(...)):
        file_extension = pathlib.Path(str(image.filename)).suffix
        uplodedFileName="CropImage"+ str(datetime.now().strftime('%Y-%m-%d %H-%M-%S')) + file_extension
       
        with open(ImageLocation+uplodedFileName, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    
        return {"filename": uplodedFileName +str(image)}


    def UplodeMultiImage(files:List[UploadFile] = File(...)):
        #file_extension = pathlib.Path(str(files.filename)).suffix
        #uplodedFileName="CropImage"+ str(datetime.now().strftime('%Y-%m-%d %H-%M-%S')) + file_extension
        
        for image in files:
    
            if len(files) >=1024 * 1024:
                raise HTTPException(status_code=403, detail="File too large")
            
            content_type = files.content_type
            if content_type not in ["image/jpeg", "image/png", "image/gif"]:
                raise HTTPException(status_code=400, detail="Invalid file type")
            
            with open(f'{image.filename}', "wb") as buffer:
                shutil.copyfileobj(image.files, buffer)
            
            #with open(ImageLocation+uplodedFileName, "wb") as buffer:
                #shutil.copyfileobj(image.files, buffer)
        

        return { "filenames": "file sucessfully uploded"}






