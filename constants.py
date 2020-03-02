# -*- coding: utf-8 -*-

# ################################""
# API PARAMETERS
# ################################""

URL = 'https://fr.openfoodfacts.org/cgi/search.pl'

# ################################""
# DATABASE PARAMETERS
# ################################""

DB_SCHEMA = 'database_schema.sql'

# ################################""
# APP PARAMETERS
# ################################""

# The following dict is used to manage the transfer of API data
# (fields = this dict keys) into MySQL database (fields = this dict values)
# by using Product object (attributes = same fields as MySQL
# database = this dict values).

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

# The following dict is used to display Product attributes
# in a user-friendly way.

PRODUCT_ATTRIBUTES = {
        "category": "Catégorie",
        "brand": "Marque",
        "name": "Nom",
        "full_name": "Nom complet",
        "quantity": "Conditionnement",
        "nutriscore": "Nutriscore",
        "url": "Lien vers la fiche OpenFoodFacts",
        "ingredients": "Ingrédients",
        "stores": "Magasins"
    }
