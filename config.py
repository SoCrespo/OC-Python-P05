# -*- coding: utf-8 -*-


#######################################
# API PARAMETERS
#######################################

URL = 'https://fr.openfoodfacts.org/cgi/search.pl'

# Choose categories that are not overlapping one another.
# This dict ensures correspondence between categories tags in API
# and their full name in the custom database.

CATEGORIES = {
    'pates-a-tartiner': 'Pâtes à tartiner',
    'matieres-grasses-a-tartiner': 'Matières grasses à tartiner',
    'pates-a-tartiner-a-base-de-levures': "pâtes à tartiner à base de levures",
    'confitures-de-fruits': 'Confitures de fruits',
    'confiture-de-lait': 'Confitures de lait',
}

API_CATEGORIES = CATEGORIES.keys()
DB_CATEGORIES = CATEGORIES.values()

# Provides matching between :
# - API fields name, on one hand
# - Product attributes and custom_database rows (they are the same),
#   on the other hand.
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

# Max number of products that must be returned by each API call for a category.
# As some products are incomplete, ensure that this limit is at least 20
# to get enough complete products.
MAX_PRODUCTS_NB = 50

#######################################
# DATABASE PARAMETERS
#######################################

# Change this dict values (strings) according to the database
# that will be used. Do not change the keys !
DB_CONNECTION_PARAMS = {
    'user': 'offuser',
    'password': 'my!pass1worD',
    'host': 'localhost',
    'database': 'offdb2020p5',
    }

DB_SCHEMA = 'project5/database_schema.sql'
