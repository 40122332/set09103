import ConfigParser
import logging
import sqlite3
from flask import Flask, request, session, g, redirect, url_for,\
render_template, flash, abort
from contextlib import closing
from logging.handlers import RotatingFileHandler

DATABASE = '/tmp/coursework.db'
DEBUG = True
SECRET_KEY = '$LR\x80\x07S\x8f\xf5\xf3\x04\xe6\xd7\xde\xa3\xcb~\xd7\x19\x9a\x17=\xf9\xae\x9a'
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

def init(app):
  config = ConfigParser.ConfigParser()
  try:
      config_location = "etc/defaults.cfg"
      config.read(config_location)
      app.config['DEBUG'] = config.get("config","debug")
      app.config['ip_address'] = config.get("config", "ip_address")
      app.config['port'] = config.get("config", "port")
      app.config['url'] = config.get("config", "url")
      app.config['log_file'] = config.get("logging", "name")
      app.config['log_location'] = config.get("logging", "location")
      app.config['log_level'] = config.get("logging", "level")
  except:
      print"Could not read configs from: ", config_location

def logs(app):
  log_pathname = app.config['log_location'] + app.config['log_file']
  file_handler = RotatingFileHandler(log_pathname, maxBytes=1024*1024*10,\
  backupCount=1024)
  file_handler.setLevel( app.config['log_level'])
  formatter = logging.Formatter("%(levelname)s|%(asctime)s|%(module)s|%(funcName)s|%(message)s")
  file_handler.setFormatter(formatter)
  app.logger.setLevel( app.config['log_level'] )
  app.logger.addHandler(file_handler)


@app.before_request
def befor_request():
  g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
      db.close()

@app.route('/config/')
def config():
  str = []
  str.append('Debug:'+app.config['DEBUG'])
  str.append('port:'+app.config['port'])
  str.append('url:'+app.config['url'])
  atr.append('ip_address:'+app.config['ip_address'])
  return '\t'.join(str)

@app.route('/', methods=['POST','GET'])
def welcome():
  if request.method == 'POST':
    return redirect(url_for('search', search=request.form['search']))
  else:
    app.logger.info("User at root page")
    cur = g.db.execute('select id,  name, size, fur_type, ear_type, origin, colour,\
    uses, url from entries order by id desc')
    entries =  [dict(id=row[0], name=row[1], size=row[2], fur_type=row[3],\
    ear_type=row[4], origin=row[5], colour=row[6], uses=row[7], url=row[8]) for row in cur.fetchall()]
    return render_template('all.html', entries=entries)

@app.route('/search/<search>')
def search(search=None):
  cur = g.db.execute('select id, name, url from entries where name like ?',["%"+search+"%"])
  entries = [dict(id=row[0], name=row[1], url=row[2])for row in cur.fetchall()]
  app.logger.info("User searched for"+search)
  return render_template('all.html', entries=entries)

@app.route('/rabbit/<id>')
def load_rabbit(id=None):
  cur = g.db.execute('select id,  name, size, fur_type, ear_type, origin, colour,\
  uses, url from entries where id=?',[id])
  entries = [dict(id=row[0], name=row[1], size=row[2], fur_type=row[3],\
  ear_type=row[4], origin=row[5], colour=row[6], uses=row[7], url=row[8]) for row in cur.fetchall()]
  app.logger.info("Rabbit with id="+id+" was loaded")
  return render_template('rabbit.html', entries=entries)

@app.route('/sort/<by>/<search>')
def search_by(search=None ,by=None):
  key = by
  cur = g.db.execute('select id,  name, size, fur_type, ear_type, origin, colour,\
  uses, url from entries where %s=?'%(key),[search])
  entries = [dict(id=row[0], name=row[1], size=row[2], fur_type=row[3],\
  ear_type=row[4], origin=row[5], colour=row[6], uses=row[7], url=row[8]) for row in cur.fetchall()]
  app.logger.info("User searched searched:"+search+" by:"+key)
  return render_template('all.html', entries=entries)

@app.route('/origin/')
def origin_select():
  cur = g.db.execute('select distinct origin from entries order by origin')
  entries = [dict(origin=row[0]) for row in cur.fetchall()]
  return render_template('origin.html', entries=entries)

@app.route('/colour/')
def colour():
  cur = g.db.execute('select distinct colour from entries order by colour')
  entries = [dict(colour=row[0]) for row in cur.fetchall()]
  return render_template('colour.html', entries=entries)

@app.route('/use/')
def use():
  cur = g.db.execute('select distinct uses from entries order by uses')
  entries = [dict(use=row[0]) for row in cur.fetchall()]
  return render_template('use.html', entries=entries)

@app.errorhandler(404)
def page_not_found(error):
  app.logger.info("error 404")
  flash(message="The page could not be found")
  return redirect(url_for('welcome'))

@app.errorhandler(405)
def method_not_alowed(error):
  flash(message="Invalid search")
  return redirect(url_for('welcome'))

if __name__ == "__main__":
  init(app)
  logs(app)
  init_db()
  app.run(
      host=app.config['ip_address'],
      port=int(app.config['port']))
