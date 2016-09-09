-------------------------------------------
-----------------Views---------------------
-------------------------------------------

--use BillyJoes database
USE BillyJoes

--View that uses Group by, Having and the aggregate function AVG
--Gives products which orders are above average
CREATE VIEW vwProductOrdersAboveAverage
AS
SELECT ProductId, OrderId, Quantity
FROM OrderDetails
GROUP BY ProductId, OrderId, Quantity
HAVING Quantity > (SELECT AVG(Quantity) FROM OrderDetails)


SELECT * FROM vwProductOrdersAboveAverage

--Query that uses Joins, aggregate functions, Group by and Order by Desc 
--(Views cannot be used with Order by so query used to demonstrate it)
--Shows product quantity and sales figures per day in descending order
SELECT  O.OrderDate,
		P.ProductName,
		SUM(D.Quantity) AS TotalQuantityOrdered,
		SUM(D.Quantity * D.UnitPrice) AS TotalPrice
FROM	Orders O
INNER jOIN
		OrderDetails D
ON		O.OrderId = D.OrderId
INNER jOIN
		Products P
ON		D.ProductId = P.ProductId
GROUP BY O.OrderDate, P.ProductName
ORDER BY O.OrderDate DESC


--View that uses aggregate function SUM and Group by
--Gives total sales figures per date
CREATE VIEW vwToTalSalesPerDate
AS
SELECT  O.OrderDate,
		SUM(D.Quantity * D.UnitPrice) AS TotalPriceOfOrders
FROM	Orders O
INNER jOIN
		OrderDetails D
ON		O.OrderId = D.OrderId
GROUP BY O.OrderDate


SELECT * FROM vwToTalSalesPerDate


--View that uses multiple joins
--Gets all Order Details into one view 
CREATE VIEW vwOrderDetails
AS
SELECT	O.OrderId,
        E.FirstName AS EmployeeName,
		E.LastName AS EmployeeLastName,
		O.OrderDate,	
		O.OrderTime,	
		C.FirstName AS CustomerName,
		C.LastName AS CustomerLastName,		
		P.ProductName,
		D.UnitPrice,		
		D.Quantity,
		(D.UnitPrice * D.Quantity) AS TotalPrice,
		O.isCash
FROM	Orders O
INNER JOIN
		Customers C
ON	    O.CustomerId = C.CustomerId
INNER JOIN
		Employees E
ON	    O.EmployeeId = E.EmployeeId
INNER JOIN
		OrderDetails D
ON	    O.OrderId = D.OrderId
INNER JOIN
		Products P
ON	    D.ProductId = P.ProductId


SELECT * FROM vwOrderDetails


--View all current products
CREATE VIEW vwCurrentProducts
AS
SELECT	ProductId,
		ProductName,
		Department,
		UnitCost,
		UnitsInStock,
		ReOrderLevel,
		isDiscontinued

FROM	Products
WHERE	isDiscontinued = 0

SELECT * FROM vwCurrentProducts


--View to see all products needing reorder
CREATE VIEW vwProductsToReOrder
AS
SELECT *
FROM   Products
WHERE  UnitsInStock <= ReOrderLevel AND isDiscontinued = 0

SELECT * FROM vwProductsToReOrder


--View to get all trade customers
CREATE VIEW vwTradeCustomers
AS
SELECT	FirstName,
		Address,
		County,
        PhoneNumber,
		isPublic
        
FROM	Customers
WHERE	isPublic = 0

SELECT * FROM vwTradeCustomers


--View to get all public customers
CREATE VIEW vwPublicCustomers
AS
SELECT	FirstName,
		LastName,
		Address,
		County,
        PhoneNumber,
		isPublic

FROM	Customers
WHERE	isPublic = 1

SELECT * FROM vwPublicCustomers

--View to see all full time employees
CREATE VIEW vwFullTimeEmployees
AS
SELECT	FirstName,
		LastName,
		Address,
		County,
        PhoneNumber,
		JobTitle,
		isFullTime

FROM	Employees
WHERE	isFullTime = 1

SELECT * FROM vwFullTimeEmployees

--View to see all part time employees
CREATE VIEW vwPartTimeEmployees
AS
SELECT	FirstName,
		LastName,
		Address,
		County,
        PhoneNumber,
		JobTitle,
		isFullTime
        
FROM	Employees
WHERE	isFullTime = 0

SELECT * FROM vwPartTimeEmployees

--View to get all morning orders
CREATE VIEW vwMorningOrders
AS
SELECT *
FROM Orders
WHERE OrderTime LIKE '%AM%'

SELECT * FROM vwMorningOrders

--View to get all afternoon orders
CREATE VIEW vwAfternoonOrders
AS
SELECT *
FROM Orders
WHERE OrderTime LIKE '%PM%'

SELECT * FROM vwAfternoonOrders

---------------------------------------------------------

