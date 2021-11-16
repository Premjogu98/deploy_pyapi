from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from flaskext.mysql import MySQL

#Create an instance of Flask
app = Flask(__name__)

#Create an instance of Flask RESTful API
api = Api(app)

#Create an instance of MySQL
mysql = MySQL()

#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'tot_auto'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Ttyd#fdh&458F4s5'
app.config['MYSQL_DATABASE_DB'] = 'master_db'
app.config['MYSQL_DATABASE_HOST'] = '185.15.211.58'

#Initialize the MySQL extension
mysql.init_app(app)


class User_validation(Resource):
    def get(self,username,password):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(f"select * from tbl_user where username='{username}' and password='{password}'")
        # rows = cursor.fetchall()
        query_result = [ dict(line) for line in [zip([ column[0] for column in cursor.description], row) for row in cursor.fetchall()] ]
        if len(query_result) > 0:
            result = {"status":True,"Data":query_result}
        else:
            result = {"status":False,"Data":'Invalid Username Password'}
            
        return jsonify(result)
    
api.add_resource(User_validation,'https://www.contractawardsinfo.com/user-validation/username=<string:username>&password=<string:password>')

if __name__ == "__main__":
    app.run(debug=True)