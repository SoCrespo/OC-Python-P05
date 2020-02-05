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


if __name__ == "__main__":
    pass
