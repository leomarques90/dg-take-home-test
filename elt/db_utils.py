import os
import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('.env')

HOST = config['envvars']['MYSQL_HOST']
USER_NAME = config['envvars']['MYSQL_USER']
PASSWORD_NAME = config['envvars']['MYSQL_PASSWORD']
DATABASE_NAME = config['envvars']['MYSQL_DATABASE']


def db_connect():
    connection = mysql.connector.connect(user=USER_NAME,
                                         password=PASSWORD_NAME,
                                         host=HOST,
                                         database=DATABASE_NAME)

    cursor = connection.cursor(buffered=True)

    return connection, cursor
