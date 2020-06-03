from flask import Flask,render_template,request,redirect,url_for,session
from flask_mysqldb import MySQL
import MySQLdb
import sys
app=Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "Harshit"
app.config['MYSQL_PASSWORD'] = "Harshit"
app.config['MYSQL_DB'] = "boycott_china"
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/alternatives')
def alternative():
    cur = mysql.connection.cursor()
    cur.execute("select * from alternatives")
    c_apps = cur.fetchall()
    return render_template('alternative.html',result = c_apps)


@app.route('/Search',methods=["POST"])
def Search():
    search = request.form['search']
    cur = mysql.connection.cursor()
    cur.execute("select * from alternatives where LOWER(chinese_app) LIKE '%"+search.lower()+"%'")
    c_apps = cur.fetchall()
    if c_apps:
        return render_template('alternative.html',result = c_apps)
    return render_template('tryAgain.html')

@app.route('/suggest')
def suggest():
    return render_template('suggest.html')

@app.route('/getBig',methods = ['POST'])
def getBig():
    Suggestion = {}
    appName = request.form['AppName']
    alternate = request.form['alternate']
    Link = request.form['Link']
    Suggestion['appName'] = appName
    Suggestion['alternate'] = alternate
    Suggestion['Link'] = Link
    print(Suggestion)
    sys.stdout.flush()
    return render_template('thanks.html')

if __name__ == "__main__":
    app.run(debug=True)