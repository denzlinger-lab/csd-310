-- =========================================
-- TEAM 3 – BACCHUS WINERY
-- FULL DATABASE BUILD SCRIPT (MILSTONE #2)
-- =========================================

CREATE DATABASE IF NOT EXISTS team3_bacchus;
USE team3_bacchus;

-- =============================
-- TABLE 1: SUPPLIER
-- =============================
CREATE TABLE Supplier (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL
);

INSERT INTO Supplier (supplier_name) VALUES
('Golden Valley Grapes'),
('Northwest Bottling Co'),
('Eagle Cork & Seal');

-- =============================
-- TABLE 2: DEPARTMENT
-- =============================
CREATE TABLE Department (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

INSERT INTO Department (department_name) VALUES
('Production'),
('Sales'),
('Logistics'),
('Management'),
('Customer Support'),
('Quality Control');

-- =============================
-- TABLE 3: EMPLOYEE (SELF-JOIN MANAGER)
-- =============================
CREATE TABLE Employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    manager_id INT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    job_title VARCHAR(100),
    hire_date DATE,
    department_id INT NOT NULL,

    FOREIGN KEY (manager_id) REFERENCES Employee(employee_id),
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

INSERT INTO Employee (manager_id, first_name, last_name, job_title, hire_date, department_id) VALUES
(NULL, 'James', 'Buzzell', 'Production Manager', '2020-01-21', 1),
(1, 'Noor', 'Al Salihi', 'Production Assistant', '2023-08-20', 1),
(1, 'Abram', 'Denzlinger', 'Logistics Coordinator', '2022-06-11', 3),
(3, 'Laura', 'Makokha', 'Sales Associate', '2021-05-10', 2),
(3, 'Sarah', 'Hill', 'Sales Manager', '2023-01-11', 2),
(4, 'Jon', 'Stone', 'Support Specialist', '2023-03-05', 5);

-- =============================
-- TABLE 4: CUSTOMER
-- =============================
CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100)
);

INSERT INTO Customer (customer_name, phone, email) VALUES
('Bacchus Wine Club Member A', '555-1010', 'a@wine.com'),
('Bacchus Wine Club Member B', '555-2020', 'b@wine.com'),
('TriCities Distributor', '555-3030', 'tri@dist.com'),
('Yakima Retailer', '555-4040', 'yak@retail.com'),
('Seattle Fine Wines', '555-5050', 'sea@finewine.com'),
('Tacoma Wine Shop', '555-6060', 'tac@shop.com');

-- =============================
-- TABLE 5: INVENTORY
-- =============================
CREATE TABLE Inventory (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100),
    quantity_on_hand INT,
    unit_price DECIMAL(10,2),
    supplier_id INT NOT NULL,

    FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id)
);

INSERT INTO Inventory (item_name, quantity_on_hand, unit_price, supplier_id) VALUES
('Chardonnay Bottles', 120, 15.00, 1),
('Cabernet Sauvignon Bottles', 200, 18.50, 1),
('Wine Cork Packs', 500, 5.50, 3),
('Bottle Labels Pack', 300, 4.00, 2),
('Shipping Boxes', 150, 2.50, 2),
('Barrel Oak Wood', 20, 250.00, 1);

-- =============================
-- TABLE 6: ORDERS
-- =============================
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    employee_id INT NOT NULL,
    order_date DATE NOT NULL,
    tracking_number VARCHAR(50) UNIQUE,

    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);

INSERT INTO Orders (customer_id, employee_id, order_date, tracking_number) VALUES
(1, 2, '2023-10-12', 'TRACK001'),
(3, 3, '2023-10-13', 'TRACK002'),
(5, 4, '2023-10-14', 'TRACK003'),
(2, 5, '2023-10-15', 'TRACK004'),
(6, 6, '2023-10-16', 'TRACK005'),
(4, 2, '2023-10-17', 'TRACK006');

-- =============================
-- TABLE 7: ORDER_ITEMS (MANY-TO-MANY)
-- =============================
CREATE TABLE Order_Items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity_ordered INT NOT NULL,
    line_total DECIMAL(10,2),

    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (item_id) REFERENCES Inventory(item_id)
);

INSERT INTO Order_Items (order_id, item_id, quantity_ordered, line_total) VALUES
(1, 1, 10, 150.00),
(1, 3, 5, 27.50),
(2, 2, 20, 370.00),
(3, 4, 50, 200.00),
(4, 5, 30, 75.00),
(5, 6, 1, 250.00);

-- =========================================
-- END OF SCRIPT
-- =========================================
