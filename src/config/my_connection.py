import mysql.connector as pymysql
from src.config.db_config import load


class MyConnection:
    __connection = None
    __cursor = None

    def __init__(self):
        data_source = load()
        self.__connection = pymysql.connect(**data_source)
        self.__cursor = self.__connection.cursor()

    def query(self, query, params):
        self.__cursor.execute(query, params)
        return self.__cursor

    def close(self):
        self.__connection.close()
