# -*- coding: utf-8 -*-

import mysql.connector
import category
import product
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

    def get_products_from_category(self, category):
        '''Returns a list of all Products from the given category.'''
        self.cursor = self.mydb.cursor(dictionary=True)
        cat_id = category.id
        products_list = []
        query = f"SELECT * FROM product WHERE cat_id ={cat_id}"
        self.cursor.execute(query)
        for row in self.cursor:
            row['category'] = category.name
            row.pop('cat_id')
            products_list.append(product.Product(row))
        self.cursor = self.mydb.cursor()
        return products_list

    def get_products_with_better_nutriscore(self, prod):
        '''Returns a list of all products with a better nutriscore
        than given product, for all categories.'''
        self.cursor = self.mydb.cursor(dictionary=True)
        nutriscore = prod.nutriscore
        substitutes_list = []
        query = (
                 f"SELECT product.*, category.name AS category FROM product "
                 f"INNER JOIN category "
                 f"ON product.cat_id = category.id "
                 f"WHERE nutriscore < '{nutriscore}'"
        )
        self.cursor.execute(query)
        for row in self.cursor:
            row.pop('id')
            substitute = product.Product(row)
            substitutes_list.append(substitute)
        self.cursor = self.mydb.cursor()
        return substitutes_list

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
        self.cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
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

    def _insert_product(self, prod):
        '''Insert 1 product in local database.'''

        prod.convert_category_to_cat_id(self.categories)
        str_keys = ", ".join(vars(prod).keys())
        values = vars(prod).values()
        escaped_values = [str(value).replace("'", "''") for value in values]
        str_values = "', '".join(escaped_values)
        query = f"INSERT INTO product ({str_keys}) VALUES ('{str_values}');"
        self.cursor.execute(query)
        self.mydb.commit()

    def _insert_products(self, products):
        '''Insert products in local database.'''
        for prod in products:
            self._insert_product(prod)
        print('Data successfully inserted in database.')

    def _convert_line_to_product(self):
        ''' Converts an SQL record to a Product object.'''
        pass


if __name__ == "__main__":
    pass
