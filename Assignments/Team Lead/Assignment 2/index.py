from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(_name_)

app = Flask(_name_)
app.secret_key = "12345"

def init_db():
    db = sqlite3.connect('Users.db')
    with open('UserScheme.sql', 'r') as schema:
        db.executescript(UserScheme.read())
    db.commit()

@app.cli.command('initdb')
def initdb_cmd():
    init_db()
    print("Initialised database.")

def get_db():
    conn = sqlite3.connect('Users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')    
def login():
    return render_template('signin.html')

@app.route('/register')
def register():
    return render_template('signup.html')

@app.route('/signup', methods = ["POST", "GET"])
def signup():
  
    if request.method == "POST":
        Username = request.form["Username"]
        EmailId = request.form["EmailId"]
        Password = request.form["Password"]
        db = get_db()
        curr = db.cursor()
        curr.execute('INSERT INTO Users (Username, EmailId, Password) VALUES (?, ?, ?);', (Username, EmailId, Password))
        db.commit()
        curr.close()
        db.close()
        return render_template('signin.html', title="signin", succ="Registration Successfull!")
    return render_template('signup.html', title='Sign Up')

@app.route('/signin', methods = ["POST", "GET"])
def signin():
    error = None
    if request.method == "POST":
        Username = request.form["Username"]
        Password = request.form["Password"]
        db = get_db()
        Users = db.execute('SELECT Password FROM Users WHERE Username = ?', (Username, )).fetchone()
        
        if Users is None:
            session['logged_in'] = False
            error = 'Incorrect Username/Password.'
        elif Password != Users['Password']:
            session['logged_in'] = False
            print(Users)
            error = 'Incorrect Password.'

        if error is None:
            session['logged_in'] = True
            return redirect(url_for('home'))
        flash(error)
        db.close()

    return render_template('signin.html', title='Sign In', error=error)
                    
if _name_ == '_main_':
    app.run(debug = True)
