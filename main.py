# -*- coding: utf-8 -*-

import custom_db_manager
import openfoodfacts_client

# opens communication with DB
db = custom_db_manager.CustomDBManager()

# Fills database if not already done
if db.is_empty:
    off_client = openfoodfacts_client.OpenFoodFactsClient()
    db.set_database(off_client.products)


# If user chooses "reset database":
# db.empty_database()
