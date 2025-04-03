CREATE DATABASE inventory;
USE inventory_db;
CREATE TABLE inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,  
    itemID VARCHAR(50) NOT NULL,     
    name VARCHAR(100) NOT NULL,        
    price DECIMAL(10,2) NOT NULL,       
    quantity INT NOT NULL,              
    category VARCHAR(100),           
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);
SHOW TABLES;
DESC inventory;
INSERT into inventory(itemID, name, price, quantity, category) 
VALUES 
('ITM001', 'Laptop', 799.99, 10, 'Electronics'),
('ITM002', 'Mouse', 19.99, 50, 'Electronics'),
('ITM003', 'Keyboard', 49.99, 30, 'Electronics');
SELECT * FROM inventory;
