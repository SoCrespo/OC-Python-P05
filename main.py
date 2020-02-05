# -*- coding: utf-8 -*-

import local_db_manager as ldbm
import config as cf


connect_params = cf.DB_CONNECTION_PARAMS

db = ldbm.LocalDBManager()
db.connect_to_database(**connect_params)
