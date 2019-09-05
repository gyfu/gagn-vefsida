#Höfundur: Huginn Þór Jóhannsson
from flask import Flask, request, url_for, render_template, redirect, g
import sqlite3

app=Flask(__name__)

DATABASE="database.db"
def get_db():
    db=getattr(g,"_database",None)
    if db is None:
        db=g._database=sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db=getattr(g,"_database",None)
    if db is not None:
        db.close()

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.errorhandler(404)
def error(e):
    return render_template("error.html")


if __name__ == "__main__":
    app.run()
