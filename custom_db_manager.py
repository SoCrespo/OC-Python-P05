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
        '''
        Create tables and fills them with API data.
        '''
        self._create_tables()
        self._fill_categories_table()
        self._get_categories_rows()
        self._insert_products(products)
        self.is_empty = False

    def get_categories(self):
        '''
        Return a list of Category objects.
        '''
        self._get_categories_rows()
        return self.categories

    def get_products_from_category(self, category):
        '''
        Return a list of all Products from the given category.
        '''
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
        '''
        Return a list of all products with a better nutriscore
        than given product, for all categories.
        '''
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
            substitute = product.Product(row)
            substitutes_list.append(substitute)
        self.cursor = self.mydb.cursor()
        return substitutes_list

    def save_substitution(self, origin, substitute):
        '''
        Save origin product and substitute in table substitution.
        '''
        query = (
                f"INSERT INTO substitution (origin_id, substitute_id) "
                f"VALUES({origin.id}, {substitute.id});"
            )
        self.cursor.execute(query)
        self.mydb.commit()

    def empty_database(self):
        '''
        Drop all tables.
        '''
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

    def get_recorded_substitutions(self):
        '''
        Return all records in table substitution,
        as a list of tuples of Products (origin, substitute).
        '''
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

        # for origin_id, substitute_id in substitutions_list:
        #     origin = self._get_product_by_id(origin_id)
        #     substitute = self._get_product_by_id(substitute_id)

    def close_database(self):
        '''
        Close database.
        '''
        self.cursor.close()

    def _is_empty(self):
        '''
        Check if database is empty (no tables). Return boolean.
        '''
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
        '''
        Create tables in database from SQL schema "DB_SCHEMA."
        '''
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
        '''
        Insert categories in categories table.
        '''
        for name, full_name in CATEGORIES.items():
            query = (
                        f"INSERT INTO category (name, full_name)"
                        f"VALUES ('{name}', '{full_name}');"
            )
            self.cursor.execute(query)
        self.mydb.commit()

    def _get_categories_rows(self):
        '''
        Set self.categories as a list of Category objects.
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
        '''
        Insert 1 product in local database.
        '''

        prod.convert_category_to_cat_id(self.categories)
        str_keys = ", ".join(vars(prod).keys())
        values = vars(prod).values()
        escaped_values = [str(value).replace("'", "''") for value in values]
        str_values = "', '".join(escaped_values)
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
        Get product of given id from product table.
        Return a Product object.
        '''
        self.cursor = self.mydb.cursor(dictionary=True)
        query = f'SELECT * FROM PRODUCT WHERE id = {id};'
        self.cursor.execute(query)
        for row in self.cursor:
            prod = product.Product(row)
        return prod


if __name__ == "__main__":
    test = CustomDBManager()
    prod = test.get_recorded_substitutions()
