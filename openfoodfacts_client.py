# -*- coding: utf-8 -*-

import requests
import params as pm


class OpenFoodFactsClient:

    def __init__(self):
        pass

    def get_products_by_category(self, category, nb):
        '''Call the OpenFoodFact API to retrieve products
        in the given category.

        Downloaded fields are defined in params.py.
        :rtype: list of nb dictionaries (1 dict = 1 product).

         '''
        url = pm.URL
        payload = pm.payloadFor(category, nb)
        req = requests.get(url, params=payload)
        return req.json().get('products')

    def get_products_by_categories(self, categories:list)  -> list:
        '''
        Call get_product_by_category() for a list of categories.
         '''
        for category in categories:
            pass



if __name__ == "__main__":
    pr = OpenFoodFactsClient()
    pat = pr.get_products_by_category('pate-a-tartiner', 10)
    print(pat)
