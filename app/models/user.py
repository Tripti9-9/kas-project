from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime
from dataclasses import field
from pickle import TRUE

class User(BaseModel):
    id :int
    Name : str
    Exp:int= Field(..., Example= 1)
    Skills: str
    Mobile_Number:int
    email:EmailStr
    password : str
    age:int
    dob:datetime
    datetime:date
    
