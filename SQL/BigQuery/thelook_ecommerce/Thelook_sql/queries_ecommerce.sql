Use thelook_ecommerce;

Select * From distribution_centers Limit 10;
SELECT * FROM products LIMIT 10;

 
-- not working yet
Select * from ga4_events Limit 10;
Select * From inventory_items Limit 10;
Select * From on_hand_inventory Limit 10;
Select * From order_items Limit 10;
Select * From orders Limit 10;
Select * From orders_by_state Limit 10;
Select * From shopping_cart Limit 10;
Select * From users Limit 10;

SELECT
COUNT(*) AS NumberOfRows,
COUNT(DISTINCT name) AS NumberofProducts
FROM `thelook_ecommerce.products`;

SELECT category, COUNT(*) AS itemCount
FROM `thelook_ecommerce.products`
GROUP BY category;

SELECT segment, COUNT(*) AS itemCount
FROM `thelook_ecommerce.products`
GROUP BY segment;

SELECT category, COUNT(*) AS itemCount
FROM `thelook_ecommerce.products`
GROUP BY category
HAVING  itemCount > 1000;

SELECT * FROM
`thelook_ecommerce.products`
TABLESAMPLE SYSTEM (10 PERCENT);

SELECT * FROM
`thelook_ecommerce.order_items`
LIMIT 10;

SELECT status, COUNT(*) AS total_orders
FROM
`thelook_ecommerce.order_items`
GROUP BY status;

SELECT user_id,
SUM(sale_price) AS total_amount
FROM
`thelook_ecommerce.order_items`
GROUP BY user_id
ORDER BY total_amount DESC
LIMIT 1;
