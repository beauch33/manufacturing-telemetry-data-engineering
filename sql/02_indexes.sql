CREATE INDEX idx_sensor_readings_ts
ON sensor_readings (reading_ts);

CREATE INDEX idx_sensor_vehicle_ts
ON sensor_readings (vehicle_id, reading_ts);
