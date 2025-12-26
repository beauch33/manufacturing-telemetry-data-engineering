CREATE TABLE sensor_readings_daily_agg (
    reading_date DATE,
    vehicle_id TEXT,
    sensor_name TEXT,
    avg_value DOUBLE PRECISION,
    max_value DOUBLE PRECISION,
    min_value DOUBLE PRECISION,
    readings_count BIGINT,
    PRIMARY KEY (reading_date, vehicle_id, sensor_name)
);

INSERT INTO sensor_readings_daily_agg
SELECT
    DATE(reading_ts),
    vehicle_id,
    sensor_name,
    AVG(reading_value),
    MAX(reading_value),
    MIN(reading_value),
    COUNT(*)
FROM sensor_readings
GROUP BY DATE(reading_ts), vehicle_id, sensor_name;
