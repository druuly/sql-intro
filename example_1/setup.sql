-- products table setup
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL
);

--insert data into products table
INSERT INTO products (name, price) VALUES ('Laptop' , 999.99);
INSERT INTO products (name, price) VALUES ('Mouse' , 25.50);
INSERT INTO products (name, price) VALUES ('Keyboard' , 75.00);
INSERT INTO products (name, price) VALUES ('Monitor' , 299.99);
INSERT INTO products (name, price) VALUES ('USB Cable' , 12.99);

-- 'python app.py' to run