from flask import Flask, render_template,redirect,request,url_for,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost:3307/covid"
db = SQLAlchemy(app)

class adminregister(db.Model):
    
    username = db.Column(db.String(20), nullable=False,primary_key=True)
    password = db.Column(db.String(20), nullable=False)

class users(db.Model):
    
    username = db.Column(db.String(20), nullable=False,primary_key=True)
    phone=db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

class volunteerlist(db.Model):
        
    username = db.Column(db.String(20), nullable=True)
    email=db.Column(db.String(20), nullable=False)
    address=db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False,primary_key=True)
    choice1=db.Column(db.String(20), nullable=False)
    choice2 = db.Column(db.String(20), nullable=False)
    choice3=db.Column(db.String(20), nullable=False)
    field = db.Column(db.String(20), nullable=False)
    idcard=db.Column(db.String(20), nullable=False)

class donors(db.Model):
        
    username = db.Column(db.String(20), nullable=True)
    age=db.Column(db.String(20), nullable=False)
    address=db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False,primary_key=True)
    bloodgroup=db.Column(db.String(20), nullable=False)
    weight = db.Column(db.String(20), nullable=False)
    gender=db.Column(db.String(20), nullable=False)
    


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        login = users.query.filter_by(username=username, password=password).first()
        if login is not None:
            return redirect(url_for("user"))
    return render_template("user_login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        phone = request.form['phone']
        password = request.form['password']

        register = users(username = username, phone=phone, password = password)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("user"))

    return render_template("register.html")



@app.route('/adminlogin')
def adminlogin(): 
    return render_template("admin_login.html")


@app.route('/admin')
def admin(): 
    return render_template("adminPage.html")


@app.route('/mumbai')
def mumbai(): 
    return render_template("mumbai.html")


@app.route('/mulund')
def mulund(): 
    return render_template("mulund.html")


@app.route('/khar')
def khar(): 
    return render_template("khar.html")


@app.route('/hospitals')
def hospitals(): 
    return render_template("hospitals.html")



@app.route("/checkadmin",methods = ['GET', 'POST'])
def checkadmin():
	if request.method == 'POST':
		username = request.form["username"]
		password = request.form["password"]
		login = adminregister.query.filter_by(username=username, password=password).first()
		if login is not None:
			return redirect(url_for("admin"))
	return render_template('adminlogin')

@app.route("/user")
def user():
    return render_template('user.html')


@app.route("/yodha")
def yodha():
    return render_template('yodha.html')

@app.route("/vol")
def volunteerform():
    return render_template('vol.html')



@app.route("/reg_volunteer",methods = ['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        address=request.form["address"]
        phone = request.form["phone"]
        choice1=request.form["choice1"]
        choice2 = request.form["choice2"]
        choice3=request.form["choice3"]
        field = request.form["field"]
        idcard=request.files["idcard"]
        
        register = volunteerlist(username=username,email=email,address=address,phone=phone,choice1=choice1,choice2=choice2,choice3=choice3,field=field,idcard=idcard.read())
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("user"))

    return render_template("vol")

@app.route("/reg_donor",methods = ['GET', 'POST'])
def blooddonor():
    if request.method == 'POST':
        username = request.form["username"]
        age = request.form["age"]
        address=request.form["address"]
        phone = request.form["phone"]
        weight=request.form["weight"]
        bloodgroup = request.form["bloodgroup"]
        gender=request.form["gender"]
        
        register = donors(username=username,age=age,address=address,phone=phone,weight=weight,bloodgroup=bloodgroup,gender=gender)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("user"))

    return render_template("bloodform")



@app.route("/bloodform")
def bloodform():
    return render_template('blood.html')
@app.route("/donate")
def donate():
    return render_template('donate.html')


app.run(debug=True)


