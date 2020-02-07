# -*- coding: utf-8 -*-

import requests
import config as cf
import product


class OpenFoodFactsClient:

    def __init__(self):
        pass

    def get_data_by_category(self, category, nb):
        '''Call the OpenFoodFact API to retrieve products
        in the given category.

        Downloaded fields are defined in config.py.
        :rtype: list of nb dictionaries (1 dict = data of 1 product).

         '''
        url = cf.URL
        payload = cf.payload_for(category, nb)
        req = requests.get(url, params=payload)
        return req.json().get('products')

    def get_data_by_categories(self, categories, nb):
        '''
        Call get_data_by_category() for a list of categories.
        return a list of dictionaries (1 dict = data of  1 product)

         '''
        list = []
        for category in categories:
            data = self.get_data_by_category(category, nb)
            for product in data:
                product['category'] = category
            list.extend(data)
        return list

    def data_to_product():
        pass
        




if __name__ == "__main__":
    pr = OpenFoodFactsClient()
    pat = pr.get_data_by_category('pate-a-tartiner', 20)
    print(pat)
