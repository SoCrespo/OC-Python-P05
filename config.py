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

API_FILTERING_FIELDS = ','.join(API_TO_PRODUCT_FIELDS.keys())

MAX_PRODUCTS_NB = 50


def payload_for(category, nb):
    return {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': category,
            'tagtype_1': 'nutrition_grade',
            'tag_contains_1': 'contains',
            'fields': API_FILTERING_FIELDS,
            'page_size': nb,
            'json': 'true',
        }


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
