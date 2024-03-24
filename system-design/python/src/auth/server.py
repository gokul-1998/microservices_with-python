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
        user_row=cur.fetchone()
        email=user_row[0]
        password=user_row[1]

        if auth.username != email or auth.password !=password:
            return 'invalid credentials',401
        else:
            return createJWT(auth.username,os.environ.get("JWT_SECRET",True))
    
    else:
        return "invalid credentials",401




def createJWT(username,secret,authz):
    return jwt.encode(
        {
            "username":username,
            "exp":datetime.datetime.now(tz=datetime.datetime.utc)+datetime.timedelta(days=1),
            "iat":datetime.datetime.now(datetime.UTC),
            "admin":authz,
        },
        secret,
        algorithm="HS256",

    )


if __name__=="__main__":
    print(__name__)
    server.run(port=5000,host="0.0.0.0")