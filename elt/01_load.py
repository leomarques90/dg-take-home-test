import logging
import os
import json

from datetime import datetime

from db_utils import db_connect


logging.basicConfig(level=logging.INFO)

def _main():
    connection, cursor = db_connect()

    refined_dir = "data/02_refined"

    for file in os.listdir(refined_dir):
        logging.info(f"Reading data from file {file}...")

        data = json.load(open(f"{refined_dir}/{file}"))

        unix_time = int(file.split("_")[1].split(".")[0])
        timestamp_value = datetime.utcfromtimestamp(unix_time)

        statement = """INSERT IGNORE INTO open_weather_raw_data
            (reference_date, data) VALUES (%s, %s)
        """

        logging.info("Inserting data into the database...")
        cursor.execute(statement, (timestamp_value, json.dumps(data)))

        connection.commit()
        logging.info(f"Data of file {file} inserted successfully!")


if __name__ == "__main__":
    _main()
