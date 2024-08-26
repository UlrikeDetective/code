Create database thelook_ecommerce;
Use thelook_ecommerce;

CREATE TABLE distribution_centers (
    id INT,
    name VARCHAR(255),
    latitude FLOAT,
    longitude FLOAT
);

CREATE TABLE ga4_events (
    id INT,
    event_type VARCHAR(255),
    uri VARCHAR(255),
    postal_code VARCHAR(20),
    traffic_source VARCHAR(255),
    browser VARCHAR(255),
    user_id INT,
    state VARCHAR(50),
    session_id VARCHAR(255),
    ip_address VARCHAR(45),
    created_at TIMESTAMP,
    sequence_number INT,
    city VARCHAR(255)
);

CREATE TABLE inventory_items (
    id INT,
    product_sku VARCHAR(255),
    product_department VARCHAR(255),
    sold_at TIMESTAMP,
    product_retail_price FLOAT,
    product_distribution_center_id INT,
    product_brand VARCHAR(255),
    product_category VARCHAR(255),
    cost FLOAT,
    created_at TIMESTAMP,
    product_id INT,
    product_name VARCHAR(255)
);

CREATE TABLE on_hand_inventory (
    on_hand_count INT,
    product_name_logistics VARCHAR(255)
);

CREATE TABLE order_items (
    id INT,
    order_id INT,
    product_id INT,
    user_id INT,
    inventory_item_id INT,
    status VARCHAR(255),
    sale_price FLOAT,
    delivered_at TIMESTAMP,
    shipped_at TIMESTAMP,
    created_at TIMESTAMP,
    returned_at TIMESTAMP
);

CREATE TABLE orders (
    order_id INT,
    user_id INT,
    status VARCHAR(255),
    gender VARCHAR(50),
    created_at TIMESTAMP,
    returned_at TIMESTAMP,
    shipped_at TIMESTAMP,
    delivered_at TIMESTAMP,
    num_of_item INT
);

CREATE TABLE orders_by_state (
    order_year INT,
    total_sales FLOAT,
    state VARCHAR(255),
    country VARCHAR(255)
);

CREATE TABLE products (
    id INT,
    sku VARCHAR(255),
    segment VARCHAR(255),
    category VARCHAR(255),
    distribution_center_id INT,
    cost FLOAT,
    retail_price FLOAT,
    name VARCHAR(255),
    brand VARCHAR(255),
    department VARCHAR(255)
);

CREATE TABLE shopping_cart (
    quantity INT,
    created_at TIMESTAMP,
    product_id INT,
    session_id VARCHAR(255)
);


CREATE TABLE taxi_trips (
    payment_type FLOAT,
    data_file_month INT,
    data_file_year INT,
    trip_type FLOAT,
    passenger_count INT,
    dropoff_location_id INT,
    tolls_amount FLOAT,
    tip_amount FLOAT,
    imp_surcharge FLOAT,
    mta_tax FLOAT,
    vendor_id INT,
    fare_amount FLOAT,
    trip_distance FLOAT,
    dropoff_datetime TIMESTAMP,
    total_amount FLOAT,
    extra FLOAT,
    rate_code FLOAT,
    store_and_fwd_flag BOOLEAN,
    pickup_location_id INT,
    pickup_datetime TIMESTAMP
);

CREATE TABLE users (
    id INT,
    created_at TIMESTAMP,
    longitude FLOAT,
    latitude FLOAT,
    gender VARCHAR(50),
    country VARCHAR(255),
    traffic_source VARCHAR(255),
    postal_code VARCHAR(20),
    first_name VARCHAR(255),
    state VARCHAR(50),
    street_address VARCHAR(255),
    age INT,
    email VARCHAR(255),
    last_name VARCHAR(255),
    city VARCHAR(255)
);

