# Homework 5

## Folder Structure

- data/raw -> All raw csv data is located here
- data/processed -> All processed parquet data is located here
- notebooks/ -> Jupyter notebook for saving and processing data is located here

## Formats used

- CSV is widely used to save raw data because of its simplicity and readability
- Parquet data is stored as a collection of columns, allowing for faster read/write operations

## Read/Write

- The .env file stores the file paths of the raw and processed data folders as DATA_DIR_RAW and DATA_DIR_PROCESSED respectively
