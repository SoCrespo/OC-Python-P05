# -*- coding: utf-8 -*-

import requests
import parameters as pm


class ProductRetriever:

    def __init__(self):
        pass

    def get_products_by_category(self, category, nb):
        '''Call the OpenFoodFact API to retrieve products in selected category.
        Downloaded fields are defined in parameters.py.
        :rtype: list of dictionaries (1 dict = 1 product)
         '''
        url = pm.URL
        payload = pm.payloadFor(category, nb)
        req = requests.get(url, params=payload)
        return req.json().get('products')


if __name__ == "__main__":
    pr = ProductRetriever()
    pat = pr.get_products_by_category('pate-a-tartiner', 10)
    print(pat)
