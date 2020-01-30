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

MAX_PRODUCTS_NB = 10

def payloadFor(category, nb):
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
