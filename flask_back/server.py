# Filename - server.py

# Import flask and datetime module for showing date and time
from flask import Flask
import datetime
from flask_sqlalchemy import SQLAlchemy


x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
app.config('SQLALCHEMY_URI') = 'postgresql://postgres:admin1234@localhost:5432/wixitasks'
db = SQLAlchemy(app)

db.init_app(app)

class DataShape(db.Model):
    id = db.Column(db.string(100))

# Route for seeing a data
@app.route('/task_data')
def server():

	# Returning an api for showing in reactjs
	return {
		"Name":"Back Dada", 
		"Age":"22",
		"Date":x, 
		"programming":"python"
		}
# Running app
if __name__ == '__main__':
	app.run(debug=True)
