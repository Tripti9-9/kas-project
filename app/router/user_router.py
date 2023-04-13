from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException, status
from app.models.user import User
from app.repository.user_repository import UserRepository
from app.repository.image_repository import imageRepository
from fastapi import File, UploadFile
from typing import List
import requests
from fastapi.responses import FileResponse
import os,csv
router = APIRouter()

IMAGEDIR = "images/" 


@router.post('/add_user')
def add_user_endpoint(user: User):
    # add user function
    UserRepository.add_user(user)
    return f'user added sucessfully, data added was: {user}'


def edit_user_endpoint(user: User):
    return None

@router.get('/Get_All_users')
def Get_All_users():
    data = UserRepository.get_all_data()
    return f'Record fetched sucessfully, Records are: {data}'


@router.post("/")
def Single_image(image: UploadFile = File(...)):
    return imageRepository.UploadSingleImage(image)

@router.post("/uplodefile")
def Multi_uplode_image(files: List[UploadFile] = File(...)):
    #imageRepository.UplodeMultiImage(files)
    return {"filenames": [file.filename for file in files]}


    









    
    

     
   



        








