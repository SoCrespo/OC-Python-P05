# -*- coding: utf-8 -*-

import mysql.connector


class LocalDBManager():

    def __init__(self):
        self.cursor = None

    def connect_to_database(self, user, password, host, database):
        if not self.cursor:
            mydb = mysql.connector.connect(
                user=user,
                passwd=password,
                host=host,
                database=database
                )
        self.cursor = mydb.cursor()

    def close_connection(self):
        self.cursor.close()

    def create_tables(self, schema):
        with open(schema, "r") as f:
            lines = f.readlines()
            print(lines)
            # for line in lines:
                # self.cursor.execute(line, multi=True)


if __name__ == "__main__":
    pass
