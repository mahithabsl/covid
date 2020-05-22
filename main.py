from flask import Flask, Markup,render_template,redirect,request,url_for,session, json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from locator import locate
import math
from plots import dataindia
from dist import district

app = Flask(__name__)


def roundup(x):
    return int(math.ceil(x / 1000.0)) * 1000


# Array of india
deaths,cases,Dates=dataindia()

#array of district
dates,mumbai,pune,nashik,nagpur,thane  =district()

district_data=[mumbai,pune,nashik,nagpur,thane]
district_name=["Mumbai","Pune","Nashik","Nagpur","Thane" ]
no_of_dis=len(district_data)
max_of_dis=[roundup(max(mumbai)),roundup(max(pune)),roundup(max(nashik)),roundup(max(nagpur)),roundup(max(thane))]

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


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
    morning=db.Column(db.String(10), nullable=False)
    afternoon=db.Column(db.String(10), nullable=False)
    evening=db.Column(db.String(10), nullable=False)


class donors(db.Model):
        
    username = db.Column(db.String(20), nullable=True)
    age=db.Column(db.String(20), nullable=False)
    address=db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False,primary_key=True)
    bloodgroup=db.Column(db.String(20), nullable=False)
    weight = db.Column(db.String(20), nullable=False)

class contactus(db.Model):
    email = db.Column(db.String(20), primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    subject = db.Column(db.String(12), nullable=False)
    query = db.Column(db.String(120), nullable=False)


@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Cases in India', max=17000, labels=bar_labels, values=bar_values,max_of_dis=max_of_dis,dates=dates,district_data=district_data,district_name=district_name,no_of_dis=no_of_dis)

@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Cases in India', max=17000, set=zip(values, labels, colors), max_of_dis=max_of_dis,dates=dates,district_data=district_data,district_name=district_name,no_of_dis=no_of_dis)

@app.route('/line')
def line():

    return render_template('line_chart.html', title='Cases in India',max_of_dis=max_of_dis,dates=dates,district_data=district_data,district_name=district_name,no_of_dis=no_of_dis)


@app.route("/")
def home():
    return render_template('index.html')
@app.route("/index")
def index():
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
            return redirect(url_for("total"))
    return render_template("user_login.html")

@app.route("/register", methods=["GET", "POST"])

def register():


    addr=locate()

    if request.method == "POST":
        username = request.form['username']
        phone = request.form['phone']
        password = request.form['password']
        register = users(username = username, phone=phone, password = password)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html",addr=addr)



@app.route('/medical')
def medical(): 
    return render_template("medical.html")


@app.route('/sealeduser')
def sealeduser(): 
    return render_template("sealedUserStatus.html")


@app.route('/adminlogin')
def adminlogin(): 
    return render_template("admin_login.html")


@app.route('/admin')
def admin(): 
    return render_template("adminPageNew.html")


@app.route('/mumbai')
def mumbai():
    query1 = volunteerlist.query.filter_by(choice1 = 'Mumbai').all()
    db.session.commit()
    print(query1)
    l1 = [i for i in query1]
    q = len(l1) 
    if q<2:
        query2 = volunteerlist.query.filter_by(choice2 = 'Mumbai').limit(2-q).all()
        l2 = [i for i in query2]
        for i in l2:
            l1.append(i)

    if len(l1) < 2:
        query3 = volunteerlist.query.filter_by(choice3 = 'Mumbai').limit(2-len(l1)).all()
        l3 = [i for i in query3]
        for i in l3:
            l1.append(i)
            
    avg = len(l1) / 3
    out = []
    last = 0.0
    while last < len(l1):
        out.append(l1[int(last):int(last + avg)])
        last += avg

    morning = out[0] #slot1
    afternoon = out[1] #slot2
    evening = out[2] #slot3 
    # print(json.dumps)
    # print(morning)
    # print(afternoon)
    # print(evening)
    # print("s")
    res1=res2=res3=[]
    for i in morning:
        ph=str(i)
        ph=(ph[15:-1] )
        userdetail=volunteerlist.query.filter_by(phone=ph).first()
        result=userdetail.__dict__
        username=(result['username'])
        phone=(result['phone'])
        email=(result['email'])
       
        res1.append((username+" "+phone+" "+email))
        print(res1)

    for i in afternoon:
        ph=str(i)
        ph=(ph[15:-1] )
        userdetail=volunteerlist.query.filter_by(phone=ph).first()
        result=userdetail.__dict__
        username=(result['username'])
        phone=(result['phone'])
        email=(result['email'])
     
       
        res2.append((username+" "+phone+" "+email))
        
        print(res2)

    for i in evening:
        ph=str(i)
        ph=(ph[15:-1] )
        userdetail=volunteerlist.query.filter_by(phone=ph).first()
        result=userdetail.__dict__
        username=(result['username'])
        phone=(result['phone'])
        email=(result['email'])
       
        print(res3)

        res3.append((username+" "+phone+" "+email))

    return render_template("mumbai.html",morning=res1[:5],afternoon=res2[5:],evening=res3[4:])



@app.route('/hospitals')
def hospitals(): 
    return render_template("hospitals.html")



@app.route('/yodhaloggedin')
def yodhaloggedins(): 
    return render_template("yodhaloggedin.html")

@app.route("/checkadmin",methods = ['GET', 'POST'])
def checkadmin():
	if request.method == 'POST':
		username = request.form["username"]
		password = request.form["password"]
		login = adminregister.query.filter_by(username=username, password=password).first()
		if login is not None:
			return redirect(url_for("admin"))
	return render_template('adminlogin')


@app.route("/crosslist")
def crosslist():
    return render_template('crosslist.html')

@app.route("/total")
def total():
    return render_template('total.html')


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
        slot=request.form.getlist('slot')
        morning=afternoon=evening=0
        print(slot)
        if '1' in slot:
            morning=1   
        if '2' in slot:
            afternoon=1
        if '3' in slot:
            evening=1

        
        print(morning,afternoon,evening)
        register = volunteerlist(username=username,email=email,address=address,phone=phone,choice1=choice1,choice2=choice2,choice3=choice3,field=field,idcard=idcard.read(),morning=morning,afternoon=afternoon,evening=evening)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("yodhaloggedins"))

    return render_template("vol.html")

@app.route("/reg_donor",methods = ['GET', 'POST'])
def blooddonor():
    if request.method == 'POST':
        username = request.form["username"]
        age = request.form["age"]
        address=request.form["address"]
        phone = request.form["phone"]
        weight=request.form["weight"]
        bloodgroup = request.form["bloodgroup"]
        # gender=request.form["gender"]
        
        register = donors(username=username,age=age,address=address,phone=phone,weight=weight,bloodgroup=bloodgroup)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("bloodform.html")



@app.route("/bloodform")
def bloodform():
    return render_template('blood.html')
@app.route("/donate")
def donate():
    return render_template('donate.html')


@app.route("/contactus", methods = ['GET', 'POST'])
def contactUs():
    if(request.method=='POST'):
        query = request.form['query']
        email = request.form['email']
        username = request.form['username']
        subject = request.form['subject']
        entry = contactus(username=username,query=query,subject =subject,email=email)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("contact.html")





app.run(debug=True)


