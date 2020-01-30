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
    'categories_tags',
    'url',
    'stores',
    'nutrition_grade_fr',
    'ingredients_text_fr'
    ])