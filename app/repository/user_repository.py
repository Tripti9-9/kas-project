from datetime import date, datetime
import os
from unittest import result
from sqlalchemy import column
from app.core.db_config import DB_Connection

class UserRepository():
    def add_user(user):
        with open('data/users.json', 'w')as f:
            # jsondata = json.dumps(user)
            f.write(str(user))

    def get_all_data():
        data_from_database = []
        conn =DB_Connection.connection()
        cursor = conn.cursor()
        sql = '''SELECT * FROM [users]''' 
        result=cursor.execute(sql)
        for row in result:
            print(row)
            data_from_database.append(row)
            print(type(row))
        return data_from_database 
    



    



    


        
    

    


    

         
        
                
       






    



        