# -*- coding: utf-8 -*-

import local_db_manager
import config as cf


connect_params = cf.DB_CONNECTION_PARAMS
schema = cf.DB_SCHEMA
categories = cf.CATEGORIES


# DATABASE CREATION 
db = local_db_manager.LocalDBManager()
db.connect_to_database(**connect_params)
db.create_tables(schema)

db.fill_category_table(categories)
