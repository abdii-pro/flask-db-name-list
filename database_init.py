from flask import Flask,render_template,request
import sqlite3 as sql

def init_db():
    conn = sql.connect("simple.db")
    c = conn.cursor()
    c.execute("""create table if not exists people(
              id integer primary key autoincrement,
              name text not null)""")
    conn.commit()
    conn.close()

init_db()