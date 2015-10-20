import sqlite3
from flask import Flask, request, session, g, redirect, url_for,\
render_template, flash, abort
from contextlib import closing

DATABASE = '/tmp/coursework.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

def init_db():
  with closing(connect_db()) as db:
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

@app.before_request
def befor_request():
  g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
      db.close()

@app.route('/')
def welcome():
  cur = g.db.execute('select id,  name, size, fur_type, ear_type, origin, colour,\
  uses from entries order by id desc')
  entries = [dict(id=row[0], name=row[1], size=row[2], fur_type=row[3],\
  ear_type=row[4], origin=row[5], colour=row[6], uses=row[7]) for row in cur.fetchall()]
  return render_template('all.html', entries=entries)

@app.route('/rabbit/<id>')
def load_rabbit(id=None):
  cur = g.db.execute('select id,  name, size, fur_type, ear_type, origin, colour,\
  uses from entries where id=?',[id])
  entries = [dict(id=row[0], name=row[1], size=row[2], fur_type=row[3],\
  ear_type=row[4], origin=row[5], colour=row[6], uses=row[7]) for row in cur.fetchall()]
  return render_template('rabbit.html', entries=entries)

if __name__ == "__main__":
  init_db()
  app.run(host='0.0.0.0', debug=True)
