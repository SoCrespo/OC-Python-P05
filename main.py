# -*- coding: utf-8 -*-

import custom_db_manager
import openfoodfacts_client


off_client = openfoodfacts_client.OpenFoodFactsClient()
db = custom_db_manager.CustomDBManager()

db.set_database(off_client.products)
# db.empty_database()
