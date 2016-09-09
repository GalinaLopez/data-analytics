-------------------------------------------
----------------Triggers-------------------
-------------------------------------------

--use BillyJoes database
USE BillyJoes

--Trigger
--Example of After Trigger for Insert using the Inserted Magic table
--Updates the units in stock of a product when a new order is placed
--and its order details are inserted into the OrderDetails table
CREATE TRIGGER trUpdateUnitsInStock ON OrderDetails FOR INSERT
AS
BEGIN
	DECLARE @ProductId int, @Quantity smallint
	SELECT  @ProductId = ProductId,
			@Quantity = Quantity
	FROM INSERTED

	UPDATE Products
	SET	   UnitsInStock -= @Quantity
	WHERE  ProductId = @ProductId
END

------------------------------------------------------------------

INSERT INTO OrderDetails
(OrderId, ProductId, UnitPrice, Quantity)
VALUES
(7,2,50,15)

SELECT * FROM OrderDetails
SELECT * FROM Products

SELECT * FROM vwProductsToReOrder

-------------------------------------------------------------------

--Trigger
--Example of After Trigger for Update using the Inserted Magic table
--Checks if a product needs to be reordered whenever its units in stock get updated in the Products table
--and if it does it inserts it into the CurrentProductToReOrder table 
CREATE TRIGGER trCheckIfProductNeedsReOrder ON Products FOR UPDATE
AS
BEGIN
	DECLARE @ProductName nvarchar(50), 
			@Department nvarchar(20), 
			@UnitCost money, 
			@UnitsInStock smallint, 
			@ReOrderLevel smallint, 
			@isDiscontinued bit

	SELECT  @ProductName = ProductName,
			@Department = Department,
			@UnitCost = UnitCost,
			@UnitsInStock = UnitsInStock,
			@ReOrderLevel = ReOrderLevel, 
			@isDiscontinued = isDiscontinued
	FROM INSERTED
	WHERE  UnitsInStock <= ReOrderLevel AND isDiscontinued = 0

	INSERT INTO CurrentProductToReOrder
	( ProductName,  Department,  UnitCost,  UnitsInStock,  ReOrderLevel,  isDiscontinued)
	VALUES
	(@ProductName, @Department, @UnitCost, @UnitsInStock, @ReOrderLevel, @isDiscontinued)		
END

----------------------------------------------------------------------------------------

--create table of CurrentProductToReOrder to be used by the trigger
CREATE TABLE CurrentProductToReOrder(			
	CurrentProductToReOrderId int IDENTITY(1,1) PRIMARY KEY NOT NULL,
	ProductName nvarchar(50) NOT NULL,
	Department nvarchar(20) NOT NULL,
	UnitCost money NOT NULL,
	UnitsInStock smallint NOT NULL,
	ReOrderLevel smallint NOT NULL,
	isDiscontinued bit NOT NULL
)

UPDATE Products
SET UnitsInStock = 3
WHERE ProductId = 2

SELECT * FROM Products
SELECT * FROM CurrentProductToReOrder

----------------------------------------------------------------------------------------