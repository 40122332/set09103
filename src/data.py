from flask import g

def add_data():
  g.db.execute('insert into entries (name, size, fur_type, ear_type, origin,\
  colour, uses) values (?,?,?,?,?,?,?)',["Alaska", "small", "short", "lopped",\
  "Germany", "Black", "Pet"])
  g.db.commit()
