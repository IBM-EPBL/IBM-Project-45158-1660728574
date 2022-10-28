from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(_name_)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/login')    
def login():
    return render_template('signin.html')

@app.route('/register')
def register():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return render_template('signout.html')

# @app.route('/signup', methods = ["POST", "GET"])
# def signup():
  
#     if request.method == "POST":
#         Username = request.form["Username"]
#         EmailId = request.form["EmailId"]
#         Password = request.form["Password"]
#         try:
#             with sqlite3.connect('user.db') as conn:
#                 cur = conn.cursor()
#                 cur.execute("INSERT into Users (Username, EmailId, Password) values (?, ?, ?)",(Username, EmailId, Password))
#                 flash('Registered successfully!', 'success')
                
#                 return render_template('signin.html')        
#         except sqlite3.IntegrityError:
#             flash("Username/EmailId already exist...", 'warning')
#             return render_template('signup.html')
#     return render_template('signin.html')

# @app.route('/signin', methods = ["POST", "GET"])
# def signin():
    
#     if request.method == "POST":
#         Username = request.form["Username"]
#         Password = request.form["Password"]
#         with sqlite3.connect('user.db') as conn:
#             cur = conn.cursor()
#             cur.execute("SELECT * from Users where Username = ? and Password = ?", (Username, Password))
#             data = cur.fetchone()
#             if data:
#                 session['logged_in'] = True
#                 for data in cur:
#                     session[Username] = data['Username']
#                     session[Password] = data['Password']
#                 return render_template('home.html')
#             else:
#                 session['logged_in'] = False
#                 flash("Invalid Username / Password...", 'warning')
#                 return render_template('signin.html')
#     return render_template('signin.html')

                    
# @app.route('/signout', methods = ["POST"])
# def signout():
#     Username = request.form['Username']
#     EmailId = request.form['EmailId']
#     Password = request.form['Password']
#     with sqlite3.connect('user.db') as conn:
#             cur = conn.cursor()
#             cur.execute("SELECT * from Users where Username = ? and Password = ?", (Username, Password))
#             data = cur.fetchone()            
#             if data:
#                 session['logged_in'] = False
#                 cur.execute("DELETE from Users where Username = ? and EmailId = ? and Password = ?", (Username, EmailId, Password))
#                 flash('You logged out!!', 'warning')
#                 return render_template('signup.html')
#             else:
#                 flash("Invalid Username / Password...", 'warning')
#                 return render_template('signout.html')
#     return render_template('signout.html')

if _name_ == '_main_':
    app.run(host='0.0.0.0' ,debug = True)
