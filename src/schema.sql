drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  name text not null,
  size text not null,
  fur_type text not null,
  ear_type text not null,
  origin text not null,
  colour txet not null,
  uses text not null,
  url text 
);
insert into entries (name, size, fur_type, ear_type, origin, colour, uses, url)
values ("Alaska","medium","short","upright","Germany","Black","textile",
"https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Alaska_schwarz.jpg/1024px-Alaska_schwarz.jpg");
insert into entries (name, size, fur_type, ear_type, origin, colour, uses, url)
values ("American","large","short","upright","United States","Blue and
white","pet",
"https://upload.wikimedia.org/wikipedia/commons/b/b8/RabbitAmericanBlue.jpg"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses, url)
values ("American Fuzzy Lop","small","long","lopped","United
Ststes","All","pet","https://upload.wikimedia.org/wikipedia/commons/0/08/Rabbit_american_fuzzy_lop_buck_white.jpg"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses, url)
values ("American Sable","large","short","upright","United
States","sable","pet","https://upload.wikimedia.org/wikipedia/commons/7/78/American_Sable.png"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses, url)
values ("Argente de
Champagne","medium","short","upright","France","Silver","pet","https://upload.wikimedia.org/wikipedia/commons/8/86/Lapin_argente.jpg"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses, url)
values ("Belgian Hare","medium","short","upright","Belgium","Black, Blue and
white","pet",
"https://upload.wikimedia.org/wikipedia/commons/2/2d/Belgische_haas_%28konijnenras%29.jpg"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses, url)
values ("Blanc de Hotot","medium","short","upright","France","white, dark rings
around eyes","textile and meat",
"https://upload.wikimedia.org/wikipedia/commons/1/18/Hotot_Rabbit%21.jpg"); 
insert into entries (name, size, fur_type, ear_type, origin, colour, uses, url)
values ("Blue of
Sint-Niklass","Any","short","upright","Belgium","Blue","textile","https://upload.wikimedia.org/wikipedia/commons/9/9f/BlvSN.jpg"); 
