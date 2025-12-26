# Manufacturing Telemetry Data Engineering Project

## Overview
This project simulates a high-throughput manufacturing telemetry data platform, similar to
systems used in autonomous vehicle and industrial environments.

It demonstrates:
- Relational schema design
- SQL performance tuning
- Python-based ETL
- Aggregation pipelines
- Production-style project structure

## Architecture
- PostgreSQL used as the operational data store
- Python scripts generate and ingest synthetic sensor telemetry
- Daily aggregation jobs create analytics-ready tables

## Schema
### Core Tables
- production_orders
- sensor_readings
- components

### Aggregated Tables
- sensor_readings_daily_agg

## Setup Instructions

### 1. Create Database
```sql
CREATE DATABASE manuf_telemetry;
