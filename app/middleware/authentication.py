from base64 import encode
import json
from unicodedata import name
import jwt
from datetime import datetime, timedelta
from app.repository.user_repository import UserRepository
from app.core.db_config import DB_Connection
import time
   # key = "secret"
    #encoded = jwt.encode({"id": "001","Name":"jack jones"}, key, algorithm="HS256")
    #print(encoded)
    #3jwt.decode(encoded, key, algorithms="HS256")

SECRET_KEY ="SECRET_KEY"
ALGORITHM = "HS256"
start_time = time.time()



class Authentication(): 
    def encode(id:str,name:str,role:str,datetime:datetime):
        payload={
                "id":"int",
                "name":str,
                "role":str,
                "datetime":datetime,
                "expiry": time.time() +20
            }
        data = UserRepository.get_data(id)     
        encoded_jwt=jwt.encode(payload,SECRET_KEY,ALGORITHM= "HS256")
        print(jwt.encoded) 
        return encoded_jwt
             
    def decode_token(encoded_string :str,id:str,name:str,role:str,datetime:datetime):
        data = UserRepository.get_data(id,name,role,datetime)
        if current_datetime - datetime <= 20:
            current_datetime= time.time()
            total_time = current_datetime-datetime
            print(" Total Execution time in seconds: ",total_time)
            unix_timestamp = time.time() 
            print(datetime.fromtimestamp(unix_timestamp)) 
 
        else:
            print('out')
        jwt.decode(encode, SECRET_KEY, algorithm=ALGORITHM)
        return UserRepository.get_user(id)
            
