from flask.ext.mysqldb import MySQL
from flaskstruct import app

#mysql configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'test'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)

def connection():
	c = mysql.connection.cursor()
	return c
def commit():
    mysql.connection.commit()