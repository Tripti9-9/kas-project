import pyodbc
from app.core import settings
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
class DB_Connection():
    def connection():
        server = settings.SQL_SERVER
        database = settings.DB_NAME 
        username = settings.USER_NAME
        password = settings.USER_PASSWORD 
        # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
        #cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
        #cnxn=pyodbc.connect('Driver={SQL Server};Server=PRAVEEN-PC;Database=Regis_form;Trusted_Connection=yes;')
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=PRAVEEN-PC;DATABASE=Test;ENCRYPT=yes;UID=sa;PWD=sonam;Trusted_Connection=No;TrustServerCertificate=Yes')
        return cnxn