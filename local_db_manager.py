# -*- coding: utf-8 -*-

import mysql.connector


class LocalDBManager():

    def __init__(self):
        self.mydb = None
        self.cursor = None

    def connect_to_database(self, user, password, host, database):
        self.mydb = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
            )
        self.cursor = self.mydb.cursor()

    def close_db(self):
        self.cursor.close()

    def create_tables(self, schema):
        with open(schema, "r") as f:
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

    def fill_category_table(self, categories):
        '''
        Take a list of categories as argument
        and insert each as a new line in category table (name).
        '''
        for category in categories:
            query = f"INSERT INTO category (name) VALUES ('{category}');"
            self.cursor.execute(query)
            self.mydb.commit()
            print(f'{category} record inserted')

    def _insert_line(self, product):
        '''
        Insert 1 product in local database.
        '''
        prod_attribs = vars(product)
        print(prod_attribs)
        for key, value in prod_attribs:
            pass
            # query = f"INSERT INTO product({', '.join(str_fields)}) VALUES ()"

    def fill_database(self, products):
        '''
        Insert products in local database.
        '''
        for product in products:
            self._insert_line(product)

    def reset_table(self):
        '''
        Empty tables and recreate its content from API data.
        '''
        pass


if __name__ == "__main__":
    pass
