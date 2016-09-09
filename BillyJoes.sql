--------Databases and Business Applications Assessment--------------
------Student: Galina Lopez		Student number: 10333429------------
------Student: Kim Kieran		Student number: 10316200------------
-------Create database for BilyJoes Hardware Suppliers--------------
--------------------------------------------------------------------

--create database called BillyJoes
CREATE DATABASE BillyJoes

--use BillyJoes database
USE BillyJoes

-------------------------------------------
-----------Table Creation------------------
-------------------------------------------

--create table of Employees
CREATE TABLE Employees
(	EmployeeId int IDENTITY(1,1) NOT NULL, --Primary key of type int autoincrement
	FirstName nvarchar(30) NOT NULL,
	LastName nvarchar(50) NOT NULL,
	Address nvarchar(100) NOT NULL,
	County nvarchar(20) NOT NULL,
	PhoneNumber nvarchar(15) NOT NULL, 
	JobTitle nvarchar(50) NOT NULL, 
	isFullTime bit NOT NULL -- 1 for FullTime, 0 for PartTime
CONSTRAINT pk_Employees PRIMARY KEY (EmployeeId)
)

--create table of Customers
CREATE TABLE Customers
(	CustomerId int IDENTITY(1,1) NOT NULL, --Primary key of type int autoincrement
	FirstName nvarchar(30) NOT NULL,
	LastName nvarchar(50) NULL,
	Address nvarchar(100) NOT NULL,
	County nvarchar(20) NULL,
	PhoneNumber nvarchar(15) NOT NULL, 
	isPublic bit NOT NULL -- 1 for Public, 0 for Trade
 CONSTRAINT pk_Customers PRIMARY KEY (CustomerId)
) 

--create table of Products
CREATE TABLE Products(			
	ProductId int IDENTITY(1,1) NOT NULL, --Primary key of type int autoincrement
	ProductName nvarchar(50) NOT NULL,
	Department nvarchar(20) NOT NULL,
	UnitCost money NOT NULL CHECK (UnitCost > 0),
	UnitsInStock smallint NOT NULL CHECK (UnitsInStock >= 0),
	ReOrderLevel smallint NOT NULL CHECK (ReOrderLevel >= 0),
	isDiscontinued bit NOT NULL -- 1 for Discontinued, 0 for Current
CONSTRAINT pk_Products PRIMARY KEY(ProductId)
)

--create table of Orders
CREATE TABLE Orders(			
	OrderId int IDENTITY(1,1) NOT NULL, --Primary key of type int autoincrement
	CustomerId int NOT NULL, --Foreign key referencing the Customers table CustomerId
	EmployeeId int NOT NULL, --Foreign key referencing the Employees table EmployeeId
	OrderDate date NOT NULL,
	OrderTime nvarchar(10) NOT NULL,
    isCash bit NOT NULL -- 1 for Cash, 0 for Credit
CONSTRAINT pk_Orders PRIMARY KEY(OrderId),
CONSTRAINT fk_OrdersCustomers FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId),
CONSTRAINT fk_OrdersEmployees FOREIGN KEY (EmployeeId) REFERENCES Employees(EmployeeId)
)

--create table of OrderDetails
CREATE TABLE OrderDetails(			
	OrderDetailsId int IDENTITY(1,1) NOT NULL, --Primary key of type int autoincrement
	OrderId int NOT NULL, --Foreign key referencing the Orders table OrderId
	ProductId int NOT NULL, --Foreign key referencing the Products table ProductId
	UnitPrice money NOT NULL CHECK (UnitPrice > 0),
	Quantity smallint NOT NULL CHECK (Quantity > 0)
CONSTRAINT pk_OrderDetails PRIMARY KEY(OrderDetailsId),
CONSTRAINT fk_OrderDetailsProducts FOREIGN KEY (ProductId) REFERENCES Products(ProductId),
CONSTRAINT fk_OrderDetailsOrders FOREIGN KEY (OrderId) REFERENCES Orders(OrderId)
)

-------------------------------------------
-----------Table Population----------------
-------------------------------------------

--populate the Employees table
INSERT INTO Employees
(FirstName, LastName, Address, County, PhoneNumber, JobTitle, isFullTime)
VALUES
('Kim', 'White', '15 Brass Street, D4', 'Dublin', '083-8476356', 'Dept Manager', 1),
('David', 'Lee', '1 Hollow Lane, D15', 'Dublin', '085-4546744', 'Stock Room', 1),
('Rita', 'Davis', '23 Navan Road, D7', 'Dublin', '086-3544677', 'Office Manager', 1),
('Jason', 'Freeman', 'Castle House, Leixlip', 'Kildare', '087-5909357', 'Shop Assistant', 0),
('David', 'Lee', '30 Dagger Lane, OldCastle', 'Meath', '089-4954666', 'Shop Assistant', 1),
('Lisa', 'Smith', '44 Henry Street, D1', 'Dublin', '085-8466866', 'Shop Assistant', 0)

SELECT * FROM Employees

--populate the Customers table
INSERT INTO Customers
(FirstName, LastName, Address, County, PhoneNumber, isPublic)
VALUES
('Des', 'Cole', '22 Land Lane, Dunboyne', 'Meath', '087-8643064', 1),
('Jacks Gardening', NULL, '1 Busy Street, D15', 'Dublin', '01-5488945', 0),
('Sparky Jobs', NULL, '10 Haven Road, D4', 'Dublin', '01-3474538', 0),
('Daisy', 'Busby', '50 Cherry Tree Lane, Celbridge', 'Kildare', '086-4389545', 1),
('Man With a Van', NULL, '26 Ongar Park, Ongar', 'Dublin', '01-8786945', 0),
('Joe', 'Duffy', '35 Ivy Street, D7', 'Dublin', '085-8974887', 1)

SELECT * FROM Customers

--populate Products Table
INSERT INTO Products
(ProductName, Department, UnitCost, UnitsInStock, ReOrderLevel, isDiscontinued)
VALUES
('Drill', 'Hardware', 45.00, 20, 5,	0),
('Saw', 'Hardware', 40.00, 17, 5, 0),
('Ladder', 'Hardware',	55.00, 30, 5, 0),
('Hard Helmet', 'Hardware',	20.00, 15, 20, 0),
('Snicker Trousers', 'Hardware', 25.00,	10,	15, 1),
('Hammer', 'DIY', 10.00, 40, 10, 0),
('Nails', 'DIY', 2.50, 200, 50, 0),
('Screwdriver', 'DIY',	15.00, 50, 10, 0),
('Flat Head Screws', 'DIY', 2.50, 200, 50, 0),
('Paint', 'DIY', 10.00,	15,	20,	1),
('Lawnmower', 'Gardening',	150.00,	7,	3, 0),
('Wooden Shed',	'Gardening', 100.00, 2,	3, 1),
('Decking', 'Gardening', 25.00, 10, 15,	0),
('Leaf Blower', 'Gardening', 35.00,	15,	5, 0),
('Plant Pots', 'Gardening',	5.00, 100, 20, 0)

SELECT * FROM Products 

--populate Orders Table
INSERT INTO Orders
(CustomerId, EmployeeId, OrderDate, OrderTime, isCash)
VALUES
(1,5,'2015-03-12','12:15 PM',1),
(2,4,'2015-03-12','02:22 PM',0),
(3,5,'2015-03-15','09:45 AM',0),
(4,4,'2015-03-12','05:30 PM',1),
(4,6,'2015-03-15','10:25 AM',1),
(5,5,'2015-03-12','08:00 PM',0),
(6,6,'2015-03-15','11:55 AM',1)

SELECT * FROM Orders

--populate OrderDetails Table
INSERT INTO OrderDetails
(OrderId, ProductId, UnitPrice, Quantity)
VALUES
(1,1,55,1),
(1,8,20,1),
(1,9,3.50,10),
(1,12,125,1),
(2,3,60,1),
(2,10,15,5),
(2,15,10,10),
(3,5,30,1),
(3,3,60,1),
(3,6,15,1),
(3,7,3,15),
(4,6,15,1),
(4,7,3,10),
(5,10,15,3),
(5,15,10,7),
(6,3,60,1),
(6,10,15,10),
(6,9,3.50,15),
(7,10,15,7),
(7,15,10,8)

SELECT * FROM OrderDetails

----------------------------------------------------