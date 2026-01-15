-- Justin Caringal
--
-- A script to declare and initialize a table for
-- a product on PVCFittingsOnline.com
--
-- Prompt provided by Service Metal Products

-- creates database and table
CREATE DATABASE IF NOT EXISTS PVCFittingsOnline;
USE PVCFittingsOnline;
CREATE TABLE Products (
    SKU VARCHAR(15) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    Material VARCHAR(50) NOT NULL,
    EndType VARCHAR(50),
    MaxPressure VARCHAR(50),
    Standards VARCHAR(100),
    SizeInches DECIMAL(10, 2) 
);

-- based off the following product:
-- https://www.pvcfittingsonline.com/collections/pvc-gate-valves/products/2-pvc-socket-gate-valve-spears-2022-020
INSERT INTO Products (
    SKU,
    Name,
    Price,
    Category,
    Material,
    EndType,
    MaxPressure,
    Standards,
    SizeInches) VALUES
    (
        '2022-020',
        '2" PVC Socket Gate Valve Spears 2022-020',
        153.04,
        'PVC Gate Valves',
        'PVC',
        'Socket',
        '200 PSI @ 73F',
        'NSF Certified for potable water use',
        2.00
    );

-- outputs table
SELECT * FROM Products;