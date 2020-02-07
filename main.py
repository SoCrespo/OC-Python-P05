# -*- coding: utf-8 -*-

import local_db_manager
import openfoodfacts_client
import config as cf


connect_params = cf.DB_CONNECTION_PARAMS
schema = cf.DB_SCHEMA
categories = cf.CATEGORIES
nb = cf.MAX_PRODUCTS_NB


# DATABASE CREATION
db = local_db_manager.LocalDBManager()
db.connect_to_database(**connect_params)
db.create_tables(schema)
db.fill_category_table(categories)

# GET PRODUCTS
off_client = openfoodfacts_client.OpenFoodFactsClient()
products_data = off_client.get_data_by_categories(categories, nb)
print(products_data)
