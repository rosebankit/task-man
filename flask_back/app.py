from flask import Flask, jsonify, request, redirect, url_for, render_template
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://username:password@localhost/dbname"
db = SQLAlchemy(app)
# Create a database engine and session
engine = create_engine('postgresql://postgres:admin1234@localhost:5432/wixitasks')
Base = declarative_base()


class Wixiteam(Base):
    __tablename__ = 'wixiteam'
    emp_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    surname = Column(String)
    gender = Column(String)
    dob = Column(Date)
    position = Column(String)
    department = Column(String)
    date_employed = Column(Date)
    location = Column(String)

    def serialize(self):
        return {
            'emp_id': self.emp_id,
            'first_name': self.first_name,
            'surname': self.surname,
            'gender': self.gender,
            'dob': self.dob,
            'position': self.position,
            'department': self.department,
            'date_employed': self.date_employed,
            'location': self.location
        }


class Wixitasks(Base):
    __tablename__ = 'wixitasks'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    allocated_to = Column(Date)
    date_allocated = Column(Date)
    description = Column(String)
    date_completed = Column(Date)
    def serialize(self):
        return {
            'id': self.id,
            'task': self.task,
            'allocated_to': self.allocated_to,
            'date_allocated': self.date_allocated,
            'description': self.description,
            'date_completed': self.date_completed,
        }


class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        admin = Administrator.query.filter_by(email=email, password=password).first()
        if admin:
            # Login successful, redirect to dashboard
            return redirect(url_for('dashboard'))
        else:
            # Login failed, show error message
            return render_template('login.html', error='Invalid email or password')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        admin = Administrator(email, password)
        db.session.add(admin)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


@app.route('/wixiteam', methods=['GET'])
def get_wixiteam_data():
    wixiteam_data = session.query(Wixiteam).all()
    return jsonify([item.serialize() for item in wixiteam_data])


@app.route('/wixitasks', methods=['GET'])
def get_wixitasks_data():
    wixitasks_data = session.query(Wixitasks).all()
    return jsonify([item.serialize() for item in wixitasks_data])

# ... rest of the code ...
