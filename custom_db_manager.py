# -*- coding: utf-8 -*-

import mysql.connector
from config import DB_CONNECTION_PARAMS, DB_SCHEMA, CATEGORIES


class CustomDBManager():

    def __init__(self):
        self.mydb = None
        self.cursor = None

    def connect_to_database(self):
        self.mydb = mysql.connector.connect(**DB_CONNECTION_PARAMS)
        self.cursor = self.mydb.cursor()

    def close_db(self):
        self.cursor.close()

    def create_tables(self):
        with open(DB_SCHEMA, "r") as f:
            lines = f.readlines()
            self.query = " ".join(lines)
        # the try...except... below is there because of a new behavior
        # of generators in Python 3.7. See here :
        # https://stackoverflow.com/questions/51700960/runtimeerror-generator-raised-stopiteration-every-time-i-try-to-run-app
        try:
            for item in self.cursor.execute(self.query, multi=True):
                # cursor.execute is an iterator if multi=True
                pass
        except RuntimeError:
            pass

    def fill_categories_table(self):
        '''
        Inserts categories in categories table .
        '''
        for category in CATEGORIES:
            query = f"INSERT INTO category (name) VALUES ('{category}');"
            self.cursor.execute(query)
            self.mydb.commit()
            print(f'{category} record inserted')

    def _insert_product(self, product):
        '''
        Insert 1 product in local database.
        '''
        prod_attribs = vars(product)
        print(prod_attribs)
        for key, value in prod_attribs:
            pass
            # query = f"INSERT INTO product({', '.join(str_fields)}) VALUES ()"

    def insert_products(self, products):
        '''
        Insert products in local database.
        '''
        for product in products:
            self._insert_product(product)

    def reset_table(self):
        '''
        Empty tables and recreate its content from API data.
        '''
        pass


if __name__ == "__main__":
    pass
