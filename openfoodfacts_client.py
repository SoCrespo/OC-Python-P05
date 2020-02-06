# -*- coding: utf-8 -*-

import requests
import config as cf


class OpenFoodFactsClient:

    def __init__(self):
        pass

    def get_products_by_category(self, category, nb):
        '''Call the OpenFoodFact API to retrieve products
        in the given category.

        Downloaded fields are defined in params.py.
        :rtype: list of nb dictionaries (1 dict = 1 product).

         '''
        url = cf.URL
        payload = cf.payload_for(category, nb)
        req = requests.get(url, params=payload)
        return req.json().get('products')

    def get_products_by_categories(self, categories, nb):
        '''
        Call get_product_by_category() for a list of categories.

         '''
        list = []
        for category in categories:
            products = self.get_products_by_category(category, nb)
            list.extend(products)
        return list


if __name__ == "__main__":
    pr = OpenFoodFactsClient()
    pat = pr.get_products_by_category('pate-a-tartiner', 20)
    print(pat)
