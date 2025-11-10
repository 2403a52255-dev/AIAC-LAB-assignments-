CREATE DATABASE IF NOT EXISTS inventory_management;
USE inventory_management;

DROP TABLE IF EXISTS Stock;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Suppliers;

CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category ENUM('Electronics', 'Accessories', 'Wearables') NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    supplier_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Stock (
    stock_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    last_updated DATE NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Suppliers (supplier_name, contact_email, phone_number) VALUES
('TechZone Distributors', 'sales@techzone.com', '9876543210'),
('Global Traders', 'info@globaltraders.com', '9123456780'),
('SmartSupply Co.', 'support@smartsupply.com', '9988776655'),
('Modern Electronics', 'hello@modernelectronics.com', '9090909090'),
('Prime Wholesalers', 'contact@primewholesalers.com', '9123456789');

INSERT INTO Products (product_name, category, price, supplier_id) VALUES
('Wireless Mouse', 'Electronics', 599.99, 1),
('Bluetooth Headphones', 'Electronics', 1299.50, 1),
('Laptop Stand', 'Accessories', 899.00, 2),
('USB-C Cable', 'Accessories', 299.00, 3),
('Smart Watch', 'Wearables', 4999.00, 4),
('LED Monitor', 'Electronics', 8999.00, 4),
('Keyboard', 'Electronics', 799.00, 2),
('Power Bank', 'Electronics', 1499.00, 3),
('Phone Case', 'Accessories', 199.00, 5),
('Tablet', 'Electronics', 15999.00, 1);

INSERT INTO Stock (product_id, quantity, last_updated) VALUES
(1, 25, '2025-11-01'),
(2, 8, '2025-11-02'),
(3, 12, '2025-11-03'),
(4, 5, '2025-11-04'),
(5, 30, '2025-11-05'),
(6, 7, '2025-11-06'),
(7, 15, '2025-11-07'),
(8, 3, '2025-11-08'),
(9, 20, '2025-11-09'),
(10, 9, '2025-11-10');

SELECT * FROM Suppliers;
SELECT * FROM Products;
SELECT * FROM Stock;

SELECT 
    P.product_id,
    P.product_name,
    P.category,
    S.quantity,
    Su.supplier_name
FROM Products P
JOIN Stock S ON P.product_id = S.product_id
JOIN Suppliers Su ON P.supplier_id = Su.supplier_id
WHERE S.quantity < 10
ORDER BY S.quantity ASC;
