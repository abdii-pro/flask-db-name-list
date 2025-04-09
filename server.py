from flask import Flask,render_template,request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        conn = sql.connect("simple.db")
        c = conn.cursor()
        c.execute("insert into people(name) values(?)",(name,))
        conn.commit()
        conn.close()
    conn = sql.connect("simple.db")
    c = conn.cursor()
    c.execute("select * from people")
    names = c.fetchall()
    conn.close()
    return render_template('index.html', names=names)

if __name__=='__main__':
    app.run(debug=True)