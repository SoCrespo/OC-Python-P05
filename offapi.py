import requests
import json

categories_json = requests.get('https://fr.openfoodfacts.org/categories.json')
categories = json.loads(categories_json.content).get('tags')
selected_categories = [i.get('name') for i in categories if 'tartiner' in i.get('name')]
print(selected_categories)



# url = 'https://fr.openfoodfacts.org/cgi/search.pl'
# payload = {
#     'action': 'process',
#     'tagtype_0': 'categories',
#     'tag_contains_0': 'contains',
#     'tag_0': 'produits-a-tartiner',
#     'tagtype_1': 'nutrition_grade',
#     'tag_contains_1': 'contains',
#     'json': 'true',
# }

# req = requests.get(url, params=payload)

# print(req.content[:10000])
