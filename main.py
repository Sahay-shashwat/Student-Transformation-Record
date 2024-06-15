from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key="STR"

from str_db import Database

db=Database()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signup.html")
def login():
    return render_template('signup.html')

@app.route("/signup", methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        try:
            name=request.form['name']
            email=request.form['email']
            password=request.form['password']
            confirm_password=request.form['confirm_password']
            flag = db.check_data_exists(email)
            if (flag == True):
                flash("USER ALREADY EXISTS!!! TRY LOGGING IN")
                print(flash())
                return redirect(url_for('signup'))
            form_data=(name,email,password)
            db.insert_record("user_details",form_data)
            return redirect('student_details.html')
        except:
            db.roll()
            return redirect('signup.html')
    else:
        return render_template('signup.html')
        


@app.route("/student_details.html")
def student_details():
    return render_template('student_details.html')

@app.route("/student_details", methods=['POST','GET'])
def post_form_data():
    if request.method == 'POST':
        try:
            student_name = request.form['fullname']
            gender = request.form['gender']
            dob = request.form['dob']
            personal_mail_id = request.form['personal_email']
            college_mail_id = request.form["college_email"]
            mobile_no = request.form["mobilenumber"]
            religion = request.form["Religion"]
            caste = request.form["caste"]
            mother_tongue = request.form["mothertongue"]
            bloodgrp = request.form["bloodgroup"]
            nationality = request.form["Nationality"]
            address = request.form["address"]
    
            form_data = (student_name, dob, bloodgrp, nationality, gender, religion, caste, address, mobile_no, personal_mail_id, college_mail_id, mother_tongue)
            db.insert_record("std_d",form_data)
        except:
            db.roll()
        finally:
            return redirect('parent_details.html')
        
@app.route("/parent_details.html")
def parent_details():
    return render_template('parent_details.html')

if __name__ == '__main__':
    app.run(debug=True)
    