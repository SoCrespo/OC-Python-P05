# -*- coding: utf-8 -*-

import custom_db_manager
import openfoodfacts_client


# ##################################################
# Database creation
# ##################################################
db = custom_db_manager.CustomDBManager()
db.connect_to_database()
db.create_tables()
db.fill_categories_table()

# ##################################################
# Data retrieving from API as Product objects
# ##################################################
off_client = openfoodfacts_client.OpenFoodFactsClient()
products = off_client.get_Products_from_API()


for product in products:
    print(f'{product.brand} {product.name}'
          f', {product.quantity}, Nutriscore : {product.nutriscore.upper()}')

# db.insert_products(products)
