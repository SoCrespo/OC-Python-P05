# -*- coding: utf-8 -*-

import mysql.connector
from config import DB_CONNECTION_PARAMS, DB_SCHEMA, CATEGORIES


class CustomDBManager():

    def __init__(self):
        self.mydb = mysql.connector.connect(**DB_CONNECTION_PARAMS)
        self.cursor = self.mydb.cursor()
        self.categories = None

    def close_database(self):
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
        for name, full_name in CATEGORIES.items():
            query = f"INSERT INTO category (name, full_name) VALUES ('{name}', '{full_name}');"
            self.cursor.execute(query)
            self.mydb.commit()
            print(f'{full_name} record inserted')

    def get_categories_rows(self):
        '''sets self.categories as a dict of categories table content,
        under the form {id: (name, full_name)}.
        '''
        query = f"SELECT * FROM category"
        self.cursor.execute(query)
        content = dict()
        for (id, name, full_name) in self.cursor:
            content.update({id: (name, full_name)})
        self.categories = content

    def _insert_product(self, product):
        '''
        Insert 1 product in local database.
        '''
        prod_attribs = vars(product)
        prod_attribs['category'] = self.categories.get()
        print(prod_attribs)
        for key, value in prod_attribs.items():
            query = f"INSERT INTO product({', '.join(str_fields)}) VALUES ()"

    # def insert_products(self, products):
    #     '''
    #     Insert products in local database.
    #     '''
    #     for product in products:
    #         self._insert_product(product)

    def reset_table(self):
        '''
        Empty tables and recreate its content from API data.
        '''
        pass


if __name__ == "__main__":
    pass
