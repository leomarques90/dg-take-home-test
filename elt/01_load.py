import logging
import os
import mysql.connector
import json

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('MYSQL_HOST')
USER_NAME = os.getenv('MYSQL_USER')
PASSWORD_NAME = os.getenv('MYSQL_PASSWORD')
DATABASE_NAME = os.getenv('MYSQL_DATABASE')

logging.basicConfig(level=logging.INFO)


def db_connect():
    connection = mysql.connector.connect(user=USER_NAME,
                                         password=PASSWORD_NAME,
                                         host=HOST,
                                         database=DATABASE_NAME)

    cursor = connection.cursor(buffered=True)

    return connection, cursor


def _main():
    connection, cursor = db_connect()

    refined_dir = "data/02_refined"

    for file in os.listdir(refined_dir):
        data = json.load(open(f"{refined_dir}/{file}"))

        unix_time = int(file.split("_")[1].split(".")[0])
        timestamp_value = datetime.utcfromtimestamp(unix_time)

        statement = """INSERT IGNORE INTO open_weather_raw_data
            (reference_date, data) VALUES (%s, %s)
        """

        cursor.execute(statement, (timestamp_value, json.dumps(data)))

        connection.commit()


if __name__ == "__main__":
    _main()
