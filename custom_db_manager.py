# -*- coding: utf-8 -*-

import mysql.connector
import category
from config import DB_CONNECTION_PARAMS, DB_SCHEMA, CATEGORIES


class CustomDBManager():

    def __init__(self):
        self.mydb = mysql.connector.connect(**DB_CONNECTION_PARAMS)
        self.cursor = self.mydb.cursor()
        self.categories = None
        self.is_empty = self._is_empty()

    def set_database(self, products):
        '''Creates tables and fills them with API data.'''
        self._create_tables()
        self._fill_categories_table()
        self._get_categories_rows()
        self._insert_products(products)
        self.is_empty = False

    def get_categories(self):
        '''Returns a list of Category objects.'''
        self._get_categories_rows()
        return self.categories

    def empty_database(self):
        '''Drops all tables.'''
        self.cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        self.cursor.execute("SELECT table_name FROM information_schema.tables \
                            WHERE table_schema = 'offdb2020p5';",)
        tables = [item[0] for item in self.cursor]
        for table in tables:
            query = f"DROP TABLE IF EXISTS {table};"
            self.cursor.execute(query)
            print(f'Table {table} deleted...')
        print('All tables deleted.')
        self.is_empty = True

    def close_database(self):
        '''Closes database.'''
        self.cursor.close()

    def _is_empty(self):
        '''Checks if database is empty (no tables). Returns boolean.'''
        tables = 'information_schema.tables'
        query = (
                 f"SELECT {tables}.table_name FROM {tables}"
                 f" WHERE {tables}.table_schema = "
                 f"'{DB_CONNECTION_PARAMS['database']}'"
                 )
        self.cursor.execute(query)
        table_number = self.cursor.fetchall()
        return len(table_number) == 0

    def _create_tables(self):
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

    def _fill_categories_table(self):
        '''Inserts categories in categories table.'''
        for name, full_name in CATEGORIES.items():
            query = (
                        f"INSERT INTO category (name, full_name)"
                        f"VALUES ('{name}', '{full_name}');"
            )
            self.cursor.execute(query)
            self.mydb.commit()

    def _get_categories_rows(self):
        '''Sets self.categories as a list of Category objects.
        These objects have following attributes : id, name, full_name.
        '''
        query = f"SELECT * FROM category"
        self.cursor.execute(query)
        categories_rows = []
        for (id, name, full_name) in self.cursor:
            categories_rows.append(
                category.Category(id, name, full_name))
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
        '''Insert 1 product in local database. '''
        self._convert_category_to_cat_id(product)
        str_keys = ", ".join(vars(product).keys())

        values = vars(product).values()
        escaped_values = [value.replace("'", "''") for value in values]
        str_values = "', '".join(escaped_values)
        query = f"INSERT INTO product ({str_keys}) VALUES ('{str_values}');"
        self.cursor.execute(query)
        self.mydb.commit()

    def _insert_products(self, products):
        '''Insert products in local database.'''
        for product in products:
            self._insert_product(product)
        print('Data successfully inserted in database.')

    def _convert_line_to_product(self):
        ''' Converts an SQL record to a Product object.'''
        pass


if __name__ == "__main__":
    pass
