drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  name text not null,
  size text not null,
  fur_type text not null,
  ear_type text not null,
  origin text not null,
  colour txet not null,
  uses text not null
);
