USE alx_book_store;

CREATE TABLE IF NOT EXISTS customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness  Ave.');

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness  Ave.');

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness  Ave.');
