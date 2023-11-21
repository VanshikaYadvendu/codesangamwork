from flask import Flask, render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/codesangam' 
db=SQLAlchemy(app)
class Users(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)
    email=db.Column(db.String,nullable=False)


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/guestmode')
def guestmode():
    return render_template('guestmode.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')    
@app.route('/register',methods=['GET','POST'])
def credentials():
    if(request.method=='POST'):
        username=request.form.get('username')
        password=request.form.get('password')
        email=request.form.get('email') 
        # This code until here was to fetch the entries for the database
        # Then we will add the data to the database
        entry=Users(username=username,password=password,email=email)
        db.session.add(entry)
        db.session.commit()
        return render_template('index.html')  # Redirect to the dashboard after successful registration


        # the entry is now added to the database
        # return redirect(url_for('/dashboard'))
    # Adjust the template name accordingly
    return render_template('register.html')     
app.run(debug=True)