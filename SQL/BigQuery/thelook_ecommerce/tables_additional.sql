


--Create empty product_orders_fulfillment table
CREATE OR REPLACE TABLE
 `thelook_ecommerce.product_orders_fulfillment`
 ( order_id INT64,
 user_id INT64,
 status STRING,
 product_id INT64,
 created_at TIMESTAMP,
 returned_at TIMESTAMP,
 shipped_at TIMESTAMP,
 delivered_at TIMESTAMP,
 cost NUMERIC,
 sale_price NUMERIC,
 retail_price NUMERIC,
 category STRING,
 name STRING,
 brand STRING,
 department STRING,
 sku STRING,
 distribution_center_id INT64);


--Create empty customers table
CREATE OR REPLACE TABLE
 `thelook_ecommerce.customers`
 ( id INT64,
 first_name STRING,
 last_name STRING,
 email STRING,
 age INT64,
 gender STRING,
 state STRING,
 street_address STRING,
 postal_code STRING,
 city STRING,
 country STRING,
 traffic_source STRING,
 created_at TIMESTAMP,
 latitude FLOAT64,
 longitude FLOAT64,
 point_location GEOGRAPHY);
 --Create empty centers table
 CREATE OR REPLACE TABLE
 `thelook_ecommerce.centers`
 ( id INT64,
 name STRING,
 latitude FLOAT64,
 longitude FLOAT64,
 point_location GEOGRAPHY);

--load the centers table from public dataset and include geography transformation
CREATE OR REPLACE TABLE
`thelook_ecommerce.centers` AS
SELECT
id,
name,
latitude,
longitude,
ST_GEOGPOINT(dcenters.longitude, dcenters.latitude) AS point_location
FROM
`bigquery-public-data.thelook_ecommerce.distribution_centers` AS dcenters;


--load the customers table from public dataset and include geography transformation
CREATE OR REPLACE TABLE
`thelook_ecommerce.customers` AS
SELECT
id,
first_name,
last_name,
email,
age,
gender,
state,
street_address,
postal_code,
city,
country,
traffic_source,
created_at,
latitude,
longitude,
ST_GEOGPOINT(users.longitude, users.latitude) AS point_location
FROM
`bigquery-public-data.thelook_ecommerce.users` AS users;
