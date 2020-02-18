# -*- coding: utf-8 -*-


#######################################
# API PARAMETERS
#######################################

URL = 'https://fr.openfoodfacts.org/cgi/search.pl'


CATEGORIES = [
    'pates-a-tartiner',
    'matieres-grasses-a-tartiner',
    'pates-a-tartiner-a-base-de-levures',
    'confitures-de-fruits',
    'confiture-de-lait'
]

API_TO_PRODUCT_FIELDS = {
    'product_name_fr': 'name',
    'generic_name_fr': 'full_name',
    'brands': 'brand',
    'quantity': 'quantity',
    'url': 'url',
    'stores': 'stores',
    'nutrition_grade_fr': 'nutriscore',
    'ingredients_text_fr': 'ingredients',
    'category': 'category'
    }

MAX_PRODUCTS_NB = 50

#######################################
# DATABASE PARAMETERS
#######################################

DB_CONNECTION_PARAMS = {
    'user': 'offuser',
    'password': 'my!pass1worD',
    'host': 'localhost',
    'database': 'offdb2020p5',
    }

DB_SCHEMA = 'project5/database_schema.sql'

DB_TABLES_NAMES = ['category', 'product', 'substitution']

# Matching between database fields and Product attributes
DB_PRODUCT_FIELDS = {'brand': 'brand',
                     'name': 'name',
                     'full_name': 'full_name',
                     'quantity': 'quantity',
                     'nutriscore': 'nutriscore',
                     'cat_id': 'category',
                     'url': 'url',
                     'ingredients': 'ingredients',
                     'stores': 'stores'}
