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
        and insert each as a new line in category table (cat_name).
        '''
        for category in categories:
            query = f"INSERT INTO category (cat_name) VALUES ('{category}');"
            self.cursor.execute(query)
            self.mydb.commit()
            print(f'{category} record inserted')

    def fill_database(self, fields, products):
        ''' Inserts products in local database.
        Fields is the list of table columns and
        products a list of Product objects.'''
        str_fields = ", ".join(fields)
        print(str_fields)
        for product in products:
            prod_attribs = vars(product)
            print(prod_attribs)
            query = f"INSERT INTO product({', '.join(str_fields)}) VALUES ()"


if __name__ == "__main__":
    pass
