import json
import pandas as pd

from db_utils import db_connect


def generate_base_dataset(cursor):
    base_dataset = []
    for row in cursor:
        data = json.loads(row[1])

        for item in data:
            location = list(item.keys())[0]
            timestamp = row[0]

            temperatures = []
            for temperature in item[location]["hourly"]:
                temperatures.append(temperature["temp"])

            base_dataset.append({
                "location": location,
                "date": timestamp,
                "temperature": temperatures,
                "min_temperature": min(temperatures),
                "max_temperature": max(temperatures),
                "sum_temperature": sum(temperatures),
                "qty_temperature": len(temperatures)
            })

    return base_dataset


def generate_max_temperature_dataset(dataset):
    dataset_one = []
    for row in dataset:
        dataset_one.append({
            "location": row["location"],
            "date": row["date"],
            "max_temperature": max(row["temperature"])
        })

    return dataset_one


def insert_data_into_dataset_one(connection, cursor, dataset):
    df = pd.DataFrame(dataset)

    df_grouped = df.groupby([df.date.dt.to_period("M"), "location"]).agg(
        {"max_temperature": "max"}).reset_index()
    df_grouped = df_grouped.astype({"date": str})

    sql = """INSERT IGNORE INTO `test_db`.`max_temperature` 
        (date, location, max_temperature) VALUES(%s,%s,%s)"""

    for i, row in df_grouped.iterrows():
        cursor.execute(sql, tuple(row))

        connection.commit()


def get_average(values):
    return round(sum(values) / len(values), 2)


def insert_data_into_dataset_two(connection, cursor, dataset):
    sql = """INSERT IGNORE INTO `test_db`.`temperature_metrics` 
        (date, sum_temperature, min_temperature, avg_temperature, 
        location_min_temperature, location_max_temperature) VALUES(%s,%s,%s,%s,%s,%s)"""

    for i, row in dataset.iterrows():
        cursor.execute(sql, tuple(row))

        connection.commit()


def generate_dataset_two(base_dataset):
    df = pd.DataFrame(base_dataset)

    df_ref = pd.DataFrame()
    df_ref = df[["date", "location", "min_temperature", "max_temperature"]]

    df_dataset_two = df.groupby("date").agg(
        {"sum_temperature": "sum",
         "qty_temperature": "sum",
         "min_temperature": "min",
         "max_temperature": "max"})

    df_dataset_two["avg_temperature"] = round(df_dataset_two["sum_temperature"] /
                                              df_dataset_two["qty_temperature"], 2)

    for new_column in ["min_temperature", "max_temperature"]:
        df_dataset_two = df_dataset_two.merge(
            df_ref[["date", new_column, "location"]], how="inner", on=["date", new_column])

    df_dataset_two = df_dataset_two.rename(
        columns={"location_x": "location_min_temperature"})
    df_dataset_two = df_dataset_two.rename(
        columns={"location_y": "location_max_temperature"})

    del df_dataset_two["qty_temperature"]
    del df_dataset_two["max_temperature"]

    return df_dataset_two


def _main():
    connection, cursor = db_connect()

    query = "SELECT * FROM `test_db`.`open_weather_raw_data`"

    cursor.execute(query)

    base_dataset = generate_base_dataset(cursor)

    dataset_one = generate_max_temperature_dataset(base_dataset)
    insert_data_into_dataset_one(connection, cursor, dataset_one)

    dataset_two = generate_dataset_two(base_dataset)
    insert_data_into_dataset_two(connection, cursor, dataset_two)


if __name__ == '__main__':
    _main()
