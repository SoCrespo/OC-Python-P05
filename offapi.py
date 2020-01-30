import requests
import json
import parameters as pm

category = pm.CATEGORIES[0]
fields = pm.FILTERING_FIELDS


url = 'https://fr.openfoodfacts.org/cgi/search.pl'
payload = {
    'action': 'process',
    'tagtype_0': 'categories',
    'tag_contains_0': 'contains',
    'tag_0': category,
    'tagtype_1': 'nutrition_grade',
    'tag_contains_1': 'contains',
    'fields': fields,
    'json': 'true',
}

req = requests.get(url, params=payload)


