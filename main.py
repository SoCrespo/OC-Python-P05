# -*- coding: utf-8 -*-

import custom_db_manager
import openfoodfacts_client


# ##################################################
# Database creation
# ##################################################
db = custom_db_manager.CustomDBManager()
db.create_tables()
db.fill_categories_table()
db.get_categories_rows()

# ##################################################
# Data retrieving from API as Product objects
# ##################################################
off_client = openfoodfacts_client.OpenFoodFactsClient()
products = off_client.get_Products_from_API()


db.insert_products(products)
