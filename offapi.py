# -*- coding: utf-8 -*-

import requests
import json
import parameters as pm


class Products():
    max_nb = pm.MAX_PRODUCTS_NB

    def __init__(self, category, nb=max_nb):
        self.category = category
        self.nb = nb
        self.content = self.get_products_by_category()

    def get_products_by_category(self):
        '''Call the OpenFoodFact API to retrieve products in selected category.
        Downloaded fields are defined in parameters.py.
        :rtype: list of dictionaries (1 dict = 1 product)
         '''
        url = pm.URL
        payload = pm.payloadFor(self.category, self.nb)
        req = requests.get(url, params=payload)
        return req.json().get('products')


if __name__ == "__main__":
    pat = Products('pate-a-tartiner-sucree', 10)

    print(pat.content)