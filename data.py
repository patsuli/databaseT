from flask import Flask
import sqlite3
from flask import Flask, render_template, redirect, url_for, request
app=Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def login():
    conn = sqlite3.connect('/home/patrik/Documents/upinniemi/merikomppanija.db')
    c = conn.cursor()
    error = None
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside
        password = request.form.get('password')
        c.execute(f"SELECT * FROM admin WHERE user = '{username}' and password = '{password}'")
        data = c.fetchone()
        print(data)
    else:
        print("penis")
        return render_template('index.html')




    return render_template('data.html', data=data)
