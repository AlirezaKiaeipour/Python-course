-- INSERT TO Customers
INSERT INTO Customers(id,name,family,city,country)
VALUES (1,"Alireza","kiaeipor","Mashhad","Iran");

INSERT INTO Customers(id,name,family,city,country)
VALUES (2,"Reza","Rezaei","Mashhad","Iran");

INSERT INTO Customers(id,name,family,city,country)
VALUES (3,"Sadegh","Sadeghi","Mashhad","Iran");

INSERT INTO Customers(id,name,family,city,country)
VALUES (4,"Hasan","Hasani","Mashhad","Iran");

INSERT INTO Customers(id,name,family,city,country)
VALUES (5,"Ali","Hosseini","Baghdad","Iraq");

-- INSERT TO Products
INSERT INTO Products(id,name,price,count)
VALUES (1,"camera",5000000,15);

INSERT INTO Products(id,name,price,count)
VALUES (2,"chips",6000,70);

INSERT INTO Products(id,name,price,count)
VALUES (3,"Speaker",250000,25);

INSERT INTO Products(id,name,price,count)
VALUES (4,"Printer hp",3000000,10);

INSERT INTO Products(id,name,price,count)
VALUES (5,"TV LED Xvision",12000000,5);

-- Show only available Products with SELECT Command
SELECT * FROM Products
WHERE count >=1;

-- Eliminate customers who are not Iranian with DELETE Command
DELETE FROM Customers
WHERE country !="Iran";

-- Reduce the price of all products by 20% with UPDATE Command
UPDATE Products
SET price = price * 80/100;

-- View customer and product tables
SELECT * FROM Products;
SELECT * FROM Customers;
