# -*- coding: utf-8 -*-

import requests
import json
import parameters as pm


class Products():

    def __init__(self, category):
        self.category = category
        self.content = self.get_products_by_category()

    def get_products_by_category(self):
        '''Call the OpenFoodFact API to retrieve products in selected category.
        Downloaded fields are defined in parameters.py.
        :rtype: list of dictionaries (1 dict = 1 product)
         '''
        fields = pm.FILTERING_FIELDS
        url = pm.URL
        payload = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': self.category,
            'tagtype_1': 'nutrition_grade',
            'tag_contains_1': 'contains',
            'fields': fields,
            'page_size': 10,
            'json': 'true',
        }
        req = requests.get(url, params=payload)
        return req.json().get('products')


if __name__ == "__main__":
    pat = Products('pate-a-tartiner')

    print(pat.content)