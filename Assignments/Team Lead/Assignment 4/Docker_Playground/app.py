from flask import Flask
import os
app = Flask(_name_)

@app.route("/")
def home():
    return "First task of Assignment 4 was done!!"

if _name_ == "_main_":
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
