CREATE TABLE sales_data (
    OrderID TEXT,
    Date TEXT,
    CustomerID TEXT,
    Product TEXT,
    Quantity INTEGER,
    UnitPrice REAL,
    ShippingAddress TEXT,
    PaymentMethod TEXT,
    OrderStatus TEXT,
    TrackingNumber TEXT,
    ItemsInCart INTEGER,
    CouponCode TEXT,
    ReferralSource TEXT,
    TotalPrice REAL
);






SELECT * FROM sales_data LIMIT 10;
SELECT COUNT(*) FROM sales_data;
SELECT SUM(TotalPrice) AS total_revenue FROM sales_data;



-- 1. Display all records
SELECT * FROM sales_data;

-- 2. Show only delivered orders
SELECT * FROM sales_data
WHERE OrderStatus='Delivered';

-- 3. Show orders with TotalPrice > 1000
SELECT * FROM sales_data
WHERE TotalPrice > 1000;

-- 4. Sort orders by TotalPrice descending
SELECT OrderID, Product, TotalPrice
FROM sales_data
ORDER BY TotalPrice DESC;

-- 5. Count total orders
SELECT COUNT(*) AS TotalOrders
FROM sales_data;

-- 6. Average order value
SELECT AVG(TotalPrice) AS AvgOrderValue
FROM sales_data;

-- 7. Total revenue
SELECT SUM(TotalPrice) AS TotalRevenue
FROM sales_data;

-- 8. Quantity sold per product
SELECT Product, SUM(Quantity) AS QuantitySold
FROM sales_data
GROUP BY Product;

-- 9. Revenue by product
SELECT Product, SUM(TotalPrice) AS Revenue
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC;

-- 10. Orders by payment method
SELECT PaymentMethod, COUNT(*) AS TotalOrders
FROM sales_data
GROUP BY PaymentMethod;

-- 11. Orders by status
SELECT OrderStatus, COUNT(*) AS TotalOrders
FROM sales_data
GROUP BY OrderStatus;

-- 12. Top spending customer
SELECT CustomerID,
SUM(TotalPrice) AS TotalSpent
FROM sales_data
GROUP BY CustomerID
ORDER BY TotalSpent DESC
LIMIT 1;

-- 13. Referral source analysis
SELECT ReferralSource,
COUNT(*) AS OrdersCount
FROM sales_data
GROUP BY ReferralSource;

-- 14. Products with revenue > 50000
SELECT Product,
SUM(TotalPrice) AS Revenue
FROM sales_data
GROUP BY Product
HAVING Revenue > 50000;

-- 15. Top 5 products by revenue
SELECT Product,
SUM(TotalPrice) AS Revenue
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;