Use thelook_ecommerce;

SET GLOBAL local_infile = 'ON';
SHOW VARIABLES LIKE 'local_infile';
SHOW VARIABLES LIKE "secure_file_priv";


LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/users.csv'
INTO TABLE users
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/taxi_trips.csv'
INTO TABLE taxi_trips
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/shopping_cart.csv'
INTO TABLE shopping_cart
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/orders.csv'
INTO TABLE orders
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/orders_by_state.csv'
INTO TABLE orders_by_state
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/order_items.csv'
INTO TABLE order_items
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/on_hand_inventory.csv'
INTO TABLE on_hand_inventory
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/inventory_items.csv'
INTO TABLE inventory_items
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/ga4_events.csv'
INTO TABLE ga4_events
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ulrike_imac_air/projects/code/SQL/BigQuery/thelook_ecommerce/Thelook_csv/thelook_ecommerce/Thelook_csv/distribution_centers.csv'
INTO TABLE distribution_centers
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
