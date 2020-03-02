# -*- coding: utf-8 -*-

# API PARAMETERS

URL = 'https://fr.openfoodfacts.org/cgi/search.pl'


MAIN_MENU_TITLE = 'MENU PRINCIPAL'

MAIN_MENU_CONTENT = [
                    'Rechercher des substituts à un produit',
                    'Afficher les substitutions enregistrées',
                    'Réinitialisation complète',
                    'Quitter'
                    ]

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

# FIELDS CONVERSION DICTIONARY
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
