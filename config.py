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

FILTERING_FIELDS = ','.join([
    'product_name_fr',
    'generic_name_fr',
    'brands',
    'quantity',
    'categories_tags',
    'url',
    'stores',
    'nutrition_grade_fr',
    'ingredients_text_fr'
    ])

MAX_PRODUCTS_NB = 10


def payload_for(category, nb):
    return {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': category,
            'tagtype_1': 'nutrition_grade',
            'tag_contains_1': 'contains',
            'fields': FILTERING_FIELDS,
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
