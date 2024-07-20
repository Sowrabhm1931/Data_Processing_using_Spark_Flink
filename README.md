# Data Processing Project

## Overview

This project demonstrates data cleaning, processing with Apache Spark and Apache Flink, both locally and on AWS EMR.

### Dataset Description

The `taxi_tripdata.csv` dataset used in this project is sourced from the New York City Taxi and Limousine Commission (TLC). It contains detailed records of taxi trips in New York City, including information such as pickup and dropoff dates and times, passenger count, trip distance, payment type, fare amount, and more.

#### Key Features:

- **VendorID**: Code indicating the provider associated with the trip record.
- **tpep_pickup_datetime**: Date and time when the meter was engaged.
- **tpep_dropoff_datetime**: Date and time when the meter was disengaged.
- **passenger_count**: Number of passengers in the vehicle.
- **trip_distance**: The trip distance in miles.
- **payment_type**: The payment method used by the passenger.
- **fare_amount**: The fare amount calculated by the meter.

This dataset provides a comprehensive view of taxi operations in NYC, useful for various analytical and machine learning tasks, such as demand prediction, fare estimation, and route optimization.

## Data Cleaning

### Steps:

1. **Read the CSV file:**
   ```python
   import pandas as pd
   import numpy as np
   df = pd.read_csv('taxi_tripdata.csv', dtype={'store_and_fwd_flag': 'category'})
    ```
2. **Convert categorical values:**
   ```python
   print(df['store_and_fwd_flag'].unique())
   df['store_and_fwd_flag'] = df['store_and_fwd_flag'].map({'Y': True, 'N': False})
   df['store_and_fwd_flag'] = df['store_and_fwd_flag'].fillna(False)
   print(df.head())
    ```
## Data Processing with Apache Spark

### Local Setup:

1. **Run the Spark script:**
   ```bash
   spark-submit --master local[2] spark_script.py
   ```

### AWS EMR Setup:

1. **Upload the Spark script to the EMR cluster.**
2. **Run the Spark script on EMR:**
   ```bash
   spark-submit --master yarn spark_script.py
   ```

## Data Processing with Apache Flink

### Local Setup:

1. **Run the Flink script:**
   ```bash
   /path/to/flink/bin/flink run -py flink_script.py
   ```

### AWS EMR Setup:

1. **Upload the Flink script to the EMR cluster.**
2. **Run the Flink script on EMR:**
   ```bash
   /usr/lib/flink/bin/flink run -py /path/to/flink_script.py
   ```

## Challenges

1. **Data Cleaning:**
   - Handled missing values in the `store_and_fwd_flag` column.
   - Converted categorical values to boolean.

2. **Running Spark and Flink:**
   - Issues with library imports and environment setups.
   - Ensuring compatibility with both local and EMR environments.

3. **Installing Jupyter Notebook:**
   - Managed dependencies and resolved issues with package installations.

## Conclusion

This project provided hands-on experience with data cleaning, and processing using Spark and Flink, and handling various challenges in different environments.
