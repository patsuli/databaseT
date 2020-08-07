from flask import Flask
import sqlite3
from flask import Flask, render_template, redirect, url_for, request
app=Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def login():
    conn = sqlite3.connect('merikomppanija.db')
    c = conn.cursor()
    error = None
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside
        password = request.form.get('password')
        c.execute(f"select * from admin where username = ? and password = ?", (username,password))
        data = c.fetchone()
        print(data)
    else:
        return render_template('index.html')




    return render_template('data.html', data=data)
