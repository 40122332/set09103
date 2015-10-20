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
insert into entries (name, size, fur_type, ear_type, origin, colour, uses)
values ("Alaska","medium","short","upright","Germany","Black","textile");
insert into entries (name, size, fur_type, ear_type, origin, colour, uses)
values ("American","large","short","upright","United States","Blue and
white","pet"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses)
values ("American Fuzzy Lop","small","long","lopped","United
Ststes","All","pet"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses)
values ("American Sable","large","short","upright","United
States","sable","pet"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses)
values ("Argente de
Champagne","medium","short","upright","France","Silver","pet"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses)
values ("Belgian Hare","medium","short","upright","Belgium","Black, Blue and
white","pet"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses)
values ("Blanc de Hotot","medium","short","upright","France","white, dark rings
around eyes","textile and meat"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses)
values ("Blue of
Sint-Niklass","Any","short","upright","Belgium","Blue","textile"); 
