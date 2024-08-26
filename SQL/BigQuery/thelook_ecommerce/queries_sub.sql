SELECT
customers.id as customer_id,
(
SELECT
MIN(ST_DISTANCE(centers.point_location, customers.point_location))/1000,
FROM
`thelook_ecommerce.centers` AS centers) AS distance_to_closest_center
FROM
`thelook_ecommerce.customers` AS customers ;
