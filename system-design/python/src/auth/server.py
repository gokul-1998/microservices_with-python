import jwt,datetime,os

from  flask import Flask,request
from flask_mysqldb import MySQL

from dotenv import load_dotenv

load_dotenv()

server=Flask(__name__)

mysql=MySQL(server)



server.config['MYSQL_HOST']=os.environ.get("MYSQL_HOST")
server.config['MYSQL_USER']=os.environ.get("MYSQL_HOST")
server.config['MYSQL_PASSWORD']=os.environ.get("MYSQL_HOST")
server.config['MYSQL_DB']=os.environ.get("MYSQL_HOST")
server.config['MYSQL_PORT']=os.environ.get("MYSQL_HOST")


@server.route("/login",methods=['POST'])
def login():
    auth=request.authorization
    if not auth:
        return "missing credentials",401
    
    # check db for username and  password
    cur=mysql.connection.cursor()
    res=cur.execute(
        "SELECT email,password from user where email=%s" ,(
        auth.username,)
    )

    if  res>0:
         
