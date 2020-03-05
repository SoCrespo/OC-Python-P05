# -*- coding: utf-8 -*-

import mysql.connector
import category
import product
from constants import DB_SCHEMA
from config import USER, PASSWORD, HOST, DATABASE, CATEGORIES


class CustomDBManager():
    '''
    Insert into / retrieve data from MySQL database.
    '''

    def __init__(self):
        self.mydb = mysql.connector.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database=DATABASE
            )
        self.is_empty = self._is_empty()
        if not self.is_empty:
            self.categories = self._get_category_objects()

    def reset_database(self, products):
        '''
        Create tables and fills them with API data.
        '''
        self._create_tables()
        self._fill_category_table()
        self.categories = self._get_category_objects()
        self._insert_products(products)
        self.is_empty = False

    def get_products_from_category(self, category):
        '''
        Return a list of all Products from the given category.
        '''
        self.cursor = self.mydb.cursor(dictionary=True)
        query = f"SELECT * FROM product WHERE cat_id ={category.id}"
        products_list = []
        self.cursor.execute(query)
        for row in self.cursor:
            row['category'] = category.name
            products_list.append(product.Product(row))
        return products_list

    def get_better_nutriscore_products(self, prod):
        '''
        Return a list of all products in MySQL database with a better
        nutriscore than prod, from same category.
        '''
        self.cursor = self.mydb.cursor(dictionary=True)
        substitutes_list = []
        query = (
                 f"SELECT product.*, category.name AS category FROM product "
                 f"INNER JOIN category "
                 f"ON product.cat_id = category.id "
                 f"WHERE nutriscore < '{prod.nutriscore}'"
                 f" AND category.name = '{prod.category}'"
        )
        self.cursor.execute(query)
        for row in self.cursor:
            substitute = product.Product(row)
            substitutes_list.append(substitute)
        return substitutes_list

    def save_substitution(self, origin, substitute):
        '''
        Save origin product and substitute in table 'substitution'.
        '''
        self.cursor = self.mydb.cursor()
        query = (
                f"INSERT INTO substitution (origin_id, substitute_id) "
                f"VALUES({origin.id}, {substitute.id});"
            )
        self.cursor.execute(query)
        self.mydb.commit()

    def get_recorded_substitutions(self):
        '''
        Return all records in table 'substitution',
        as a list of tuples of Products (origin, substitute).
        '''
        self.cursor = self.mydb.cursor()
        query = ('SELECT * FROM substitution')
        substitutions_by_id = []
        self.cursor.execute(query)
        for row in self.cursor:
            substitutions_by_id.append(row)
        get_prod = self._get_product_by_id
        substitutions = [
            (get_prod(origin), get_prod(substitute))
            for (origin, substitute) in substitutions_by_id
            ]
        return substitutions

    def empty_database(self):
        '''
        Drop all tables.
        '''
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        self.cursor.execute("SELECT table_name FROM information_schema.tables \
                            WHERE table_schema = 'offdb2020p5';",)
        tables = [item[0] for item in self.cursor]
        for table in tables:
            query = f"DROP TABLE IF EXISTS {table};"
            self.cursor.execute(query)
            print(f'Suppression de la table {table}...')
        self.cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        print('Toutes les tables ont été supprimées.')
        self.is_empty = True

    def close_database(self):
        '''
        Close connection to database.
        '''
        self.cursor.close()

    def _is_empty(self):
        '''
        Check if database is empty (no tables). Return boolean.
        '''
        self.cursor = self.mydb.cursor()
        tables = 'information_schema.tables'
        query = (
                 f"SELECT {tables}.table_name FROM {tables}"
                 f" WHERE {tables}.table_schema = "
                 f"'{DATABASE}'"
                 )
        self.cursor.execute(query)
        table_number = self.cursor.fetchall()
        return len(table_number) == 0

    def _create_tables(self):
        '''
        Create tables in database from SQL schema "DB_SCHEMA."
        '''
        self.cursor = self.mydb.cursor()
        query = ''
        with open(DB_SCHEMA, "r") as f:
            lines = f.readlines()
            query = " ".join(lines)
        # the try...except... below is there because of a new behavior
        # of generators in Python 3.7. See here :
        # https://stackoverflow.com/questions/51700960/runtimeerror-generator-raised-stopiteration-every-time-i-try-to-run-app
        try:
            for item in self.cursor.execute(query, multi=True):
                pass
        except RuntimeError:
            pass

    def _fill_category_table(self):
        '''
        Insert categories (listed in CATEGORIES) into 'category' table.
        '''
        self.cursor = self.mydb.cursor()
        for name, full_name in CATEGORIES.items():
            query = (
                        f"INSERT INTO category (name, full_name)"
                        f"VALUES ('{name}', '{full_name}');"
            )
            self.cursor.execute(query)
        self.mydb.commit()

    def _get_category_objects(self):
        '''
        Creates self.categories as a list of Category objects.
        These objects have following attributes : id, name, full_name.
        '''
        self.cursor = self.mydb.cursor()
        query = f"SELECT * FROM category"
        self.cursor.execute(query)
        categories_objects = []
        for (id, name, full_name) in self.cursor:
            categories_objects.append(
                category.Category(id, name, full_name))
        return categories_objects

    def _insert_product(self, prod):
        '''
        Insert 1 product in local database.
        '''
        prod.convert_category_to_cat_id(self.categories)
        str_keys = ", ".join(vars(prod).keys())
        values = vars(prod).values()
        escaped_values = [str(value).replace("'", "''") for value in values]
        str_values = "', '".join(escaped_values)
        self.cursor = self.mydb.cursor()
        query = f"INSERT INTO product ({str_keys}) VALUES ('{str_values}');"
        self.cursor.execute(query)
        self.mydb.commit()

    def _insert_products(self, products):
        '''
        Insert products (= list of Product) in local database.
        '''
        for prod in products:
            self._insert_product(prod)
        print('Les données ont été correctement intégrées à la base.')

    def _get_product_by_id(self, id):
        '''
        Get product of given id from 'product' table.
        Return a Product object.
        '''
        self.cursor = self.mydb.cursor(dictionary=True)
        query = f'SELECT * FROM PRODUCT WHERE id = {id};'
        self.cursor.execute(query)
        for row in self.cursor:
            prod = product.Product(row)
        return prod


if __name__ == "__main__":
    pass
