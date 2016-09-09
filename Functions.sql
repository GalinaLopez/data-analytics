-------------------------------------------
---------------Functions-------------------
-------------------------------------------

--use BillyJoes database
USE BillyJoes

--Scalar Function that accepts multiple parameters and returns a single value of type money
--Returns the Sales figure of a particular product over a particular period of time
CREATE FUNCTION udfGetProductSalesOverTime
(@ProductName nvarchar(50), @BeginDate date, @EndDate date)
RETURNS money
AS
BEGIN
	DECLARE @Sales money
	SELECT  @Sales = SUM(D.Quantity * D.UnitPrice)
	FROM	Orders O
	INNER JOIN
			OrderDetails D
	ON	    O.OrderId = D.OrderId
	INNER JOIN
			Products P
	ON	    D.ProductId = P.ProductId
	WHERE	P.ProductName = @ProductName AND 
			O.OrderDate BETWEEN @BeginDate AND @EndDate
	RETURN  @Sales
END

SELECT dbo.udfGetProductSalesOverTime('Nails','2015-01-01','2015-12-31')


--Scalar Function that accepts a single parameter and returns a single value of type int
--Returns the reorder quantity of a particular product
CREATE FUNCTION udfGetReOrderQuantity
(@ProductName nvarchar(50))
RETURNS int
AS
BEGIN
	DECLARE @Quantity int
	SELECT  @Quantity = (ReOrderLevel - UnitsInStock)
	FROM	Products 
	WHERE	ProductName = @ProductName 
	RETURN  @Quantity
END

SELECT dbo.udfGetReOrderQuantity('Paint')


--Nested Scalar Functions
--It returns the cost figure of the reorder of a particular product
CREATE FUNCTION udfGetReOrderCost
(@ProductName nvarchar(50))
RETURNS money
AS
BEGIN
	DECLARE @Cost money
	SELECT  @Cost = dbo.udfGetReOrderQuantity(@ProductName) * UnitCost
	FROM	Products  
	WHERE	ProductName = @ProductName 
	RETURN  @Cost
END

SELECT dbo.udfGetReOrderCost('Decking')


-- Table valued Function taking single parameter
--Returns a table of all customers from a particular county
CREATE FUNCTION udfGetCustomersOfCounty
(@County nvarchar(20))
RETURNS Table
AS
RETURN
SELECT
		FirstName,
		LastName,
		Address,
		County,
        PhoneNumber,
		isPublic
FROM
		Customers
WHERE
		County = @County

SELECT * FROM udfGetCustomersOfCounty('Kildare')


--Table valued Function taking multiple parameters
--Returns a table of all employees of a particlar job title and contract type
CREATE FUNCTION udfGetEmployeesOfJobTitle
(@JobTitle nvarchar(50), @isFullTime bit)
RETURNS Table
AS
RETURN
SELECT
		FirstName,
		LastName,
		Address,
		County,
        PhoneNumber,
		JobTitle,
		isFullTime
FROM
		Employees
WHERE
		JobTitle = @JobTitle AND isFullTime = @isFullTime

SELECT * FROM udfGetEmployeesOfJobTitle('Shop Assistant', 0)

--------------------------------------------------------------------------
