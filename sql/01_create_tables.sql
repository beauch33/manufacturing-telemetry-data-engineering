CREATE TABLE production_orders (
    id SERIAL PRIMARY KEY,
    order_number TEXT UNIQUE,
    vehicle_id TEXT,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    status TEXT
);

CREATE TABLE sensor_readings (
    id BIGSERIAL PRIMARY KEY,
    vehicle_id TEXT,
    sensor_name TEXT,
    reading_ts TIMESTAMP,
    reading_value DOUBLE PRECISION
);

CREATE TABLE components (
    id SERIAL PRIMARY KEY,
    component_code TEXT UNIQUE,
    description TEXT,
    vehicle_id TEXT
);
