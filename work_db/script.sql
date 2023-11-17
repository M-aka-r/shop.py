CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name VARCHAR(50)
);
INSERT INTO categories(name) VALUES ('Electronic');
INSERT INTO categories(name) VALUES ('Furniture');
INSERT INTO categories(name) VALUES ('Toys');
