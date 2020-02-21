# -*- coding: utf-8 -*-

import mysql.connector
import row_translator
from config import DB_CONNECTION_PARAMS, DB_SCHEMA, CATEGORIES


class CustomDBManager():

    def __init__(self):
        self.mydb = mysql.connector.connect(**DB_CONNECTION_PARAMS)
        self.cursor = self.mydb.cursor()
        self.categories = None

    def close_database(self):
        self.cursor.close()

    def create_tables(self):
        query = ''
        with open(DB_SCHEMA, "r") as f:
            lines = f.readlines()
            query = " ".join(lines)
        # the try...except... below is there because of a new behavior
        # of generators in Python 3.7. See here :
        # https://stackoverflow.com/questions/51700960/runtimeerror-generator-raised-stopiteration-every-time-i-try-to-run-app
        try:
            for item in self.cursor.execute(query, multi=True):
                # cursor.execute is an iterator if multi=True
                pass
        except RuntimeError:
            pass

    def fill_categories_table(self):
        '''
        Inserts categories in categories table .
        '''
        for name, full_name in CATEGORIES.items():
            query = (
                        f"INSERT INTO category (name, full_name)"
                        f"VALUES ('{name}', '{full_name}');"
            )
            self.cursor.execute(query)
            self.mydb.commit()

    def get_categories_rows(self):
        '''sets self.categories as a list of RowTranslator objects. These
        objects have following attributes : id, name, full_name.
        '''
        query = f"SELECT * FROM category"
        self.cursor.execute(query)
        categories_rows = []
        for (id, name, full_name) in self.cursor:
            categories_rows.append(
                row_translator.Rowtranslator(id, name, full_name))
        self.categories = categories_rows

    def _convert_category_to_cat_id(self, product):
        '''
        For a Product instance, creates cat_id attribute (according to
        category table) and deletes category attribute.
        '''
        product.cat_id = str([item.id for item in self.categories
                             if item.name == product.category][0])
        del(product.category)

    def _insert_product(self, product):
        '''
        Insert a product in local database.
        '''
        self._convert_category_to_cat_id(product)
        str_keys = ", ".join(vars(product).keys())

        values = vars(product).values()
        escaped_values = [value.replace("'", "''") for value in values]
        str_values = "', '".join(escaped_values)
        query = f"INSERT INTO product ({str_keys}) VALUES ('{str_values}');"

        print(query)
        self.cursor.execute(query)
        self.mydb.commit()

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
