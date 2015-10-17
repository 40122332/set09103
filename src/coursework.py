import sqlite3
from flask import Flask, request, session, g, redirect, url_for,
render_template, flash
from contextlib import closing

DATABASE = '/tmp/coursework.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)

def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

def init_db():
  with closing(connect_db()) as db:
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

@app.before_request
def before_request():
  g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
      db.close()

@app.route('/')
def welcome():
  cur = g.db.execute('select name, size, fur_type, ear_type, origin, colour,\
  uses from entries order by id desc')
  entries = [dict(name=row[0], size=[1], fur_type=[2], ear_type=[3],
  origin=[4], colour=[5], uses=[6]) for row in cur.fetchall()]
  return render_template('base.html', entries=entries)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
