-------------------------------------------
-----------Stored Procedures---------------
-------------------------------------------

--use BillyJoes database
USE BillyJoes

--Stored Procedures with multiple parameters for entering data
--Stored Procedure to insert products into the Products table
CREATE PROCEDURE uspAddProduct
                (@ProductName nvarchar(50),
                 @Department nvarchar(20),
                 @UnitCost money,
                 @UnitsInStock smallint,
                 @ReOrderLevel smallint,
                 @isDiscontinued bit)
AS
INSERT INTO Products
            (ProductName,
             Department,
             UnitCost,
             UnitsInStock,
             ReOrderLevel,
             isDiscontinued)
 VALUES
            (@ProductName,
             @Department,
             @UnitCost,
             @UnitsInStock,
             @ReOrderLevel,
             @isDiscontinued)
GO

EXECUTE uspAddProduct
             @ProductName = 'Rake',
             @Department = 'Gardening',
             @UnitCost = 15.00,
             @UnitsInStock = 25,
             @ReOrderLevel = 10,
             @isDiscontinued = 0

SELECT * FROM Products

--Stored Procedure to insert orders into the Orders table
CREATE PROCEDURE uspAddOrder
                (@CustomerId int,
                 @EmployeeId int,
                 @OrderDate date,
				 @OrderTime nvarchar(10),
                 @isCash bit)
AS
INSERT INTO Orders
            (CustomerId,
             EmployeeId,
             OrderDate,
			 OrderTime,
             isCash)
VALUES
            (@CustomerId,
             @EmployeeId,
             @OrderDate,
			 @OrderTime,
             @isCash)
GO

EXECUTE uspAddOrder
             @CustomerId = 1,
             @EmployeeId = 4,
             @OrderDate = '2015-03-17',
			 @OrderTime = '10:25 AM',
             @isCash = 1

SELECT * FROM Orders


--Stored Procedure to insert customers into the Customers table
CREATE PROCEDURE uspAddCustomer
                (@FirstName nvarchar(30),
                 @LastName nvarchar(50),
                 @Address nvarchar(100),
                 @County nvarchar(20),
                 @PhoneNumber nvarchar(15),
                 @isPublic bit)
AS
INSERT INTO Customers
            (FirstName,
             LastName,
             Address,
             County,
             PhoneNumber,
             isPublic)
 VALUES
            (@FirstName,
             @LastName,
             @Address,
             @County,
             @PhoneNumber,
             @isPublic)
GO

EXECUTE uspAddCustomer
            @FirstName = 'Jason',
            @LastName = 'Johns',
            @Address = 'Castle House, Trim',			 
            @County = 'Meath',
            @PhoneNumber = '01 8222278',
            @isPublic = 1

SELECT * FROM Customers

--Stored Procedure to insert employees into the Employees table
CREATE PROCEDURE uspAddEmployee
                (@FirstName nvarchar(30),
                 @LastName nvarchar(50),
                 @Address nvarchar(100),
				 @County nvarchar(20),
                 @PhoneNumber nvarchar(15),
                 @JobTitle nvarchar(50),
                 @isFullTime bit)
AS
INSERT INTO Employees
            (FirstName,
             LastName,
             Address,
             County,
             PhoneNumber,
			 JobTitle,
             isFullTime)
 VALUES
            (@FirstName,
             @LastName,
             @Address,
             @County,
             @PhoneNumber,
			 @JobTitle,
             @isFullTime)
GO

EXECUTE uspAddEmployee
			@FirstName = 'Amy',
            @LastName = 'Davis',
            @Address = '22 Color Lane, D8',
            @County = 'Dublin',
            @PhoneNumber = '087 3247865',
			@JobTitle = 'Shop Assistant',
            @isFullTime = 1

UPDATE Employees
SET JobTitle = 'Shop Supervisor'
WHERE EmployeeId = 5

DELETE FROM Employees
WHERE EmployeeId = 7

SELECT * FROM Employees

--Stored Procedure with Left Join
--Allows us to see all customers details whether they have orders or not
CREATE PROCEDURE uspGetCustomerDetails
AS
SELECT 
		C.CustomerId,
		C.FirstName,
		C.LastName,
		C.PhoneNumber,
		O.OrderId,
		O.OrderDate,
		O.OrderTime
FROM
		Customers C
LEFT JOIN
		Orders O

ON C.CustomerId = O.CustomerId
GO

uspGetCustomerDetails


--Stored Procedure with default parameter and ISNULL function
--Allows us to see all orders of a particular county
CREATE PROCEDURE uspGetOrdersByCounty
@County nvarchar(20) = NULL
AS
SELECT *
FROM
		Customers C
INNER JOIN
		Orders O

ON C.CustomerId = O.CustomerId
WHERE C.County = ISNULL(@County, County)
GO

uspGetOrdersByCounty 'Dublin'


--Stored Procedure with default parameter, ISNULL function and % wildcard character
--Allows us to see all employees details of a particular job title or partof
CREATE PROCEDURE uspGetEmployeesDetailsByJobTitle
@Title nvarchar(50) = NULL
AS
SELECT *
FROM
		Employees E
LEFT jOIN
		Orders O
ON E.EmployeeId = O.EmployeeId
WHERE E.JobTitle LIKE '%' + ISNULL(@Title, E.JobTitle) + '%'
GO

uspGetEmployeesDetailsByJobTitle 'Shop'


--Stored Procedure with output parameter
--Allows to get the number of customers from a particular county
CREATE PROCEDURE uspGetCustomerCountByCounty
@County nvarchar(20),
@Count int OUTPUT
AS
SELECT @Count = count(*)
FROM Customers
WHERE County = @County
GO

DECLARE @Count int
EXECUTE uspGetCustomerCountByCounty 'Dublin', @Count OUTPUT
SELECT @Count AS CustomerCount

SELECT * FROM Customers

------------------------------------------------------------