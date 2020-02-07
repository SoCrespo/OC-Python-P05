# -*- coding: utf-8 -*-

import requests
import config as cf
import product


class OpenFoodFactsClient:
    '''Retrieve data from openFoodFactAPI and converts them
    in a list of Product objects.'''

    def __init__(self):
        pass

    def get_data_by_category(self, category, nb):
        '''
        Call the OpenFoodFact API to retrieve products
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
        Return a list of dictionaries (1 dict = data of  1 product)
        Add the 'category' key in each dict.

         '''
        list = []
        for category in categories:
            data = self.get_data_by_category(category, nb)
            for item in data:
                item['category'] = category
            list.extend(data)
        return list

    def change_data_keys(self, list):
        '''
        Returns a list of product data (dict) where keys are translated
        into those expected by Product class.
        '''
        tags = cf.CONVERTING_FIELDS
        conv_list = [{tags[key]: value for key, value in product_data.items()}
                     for product_data in list]
        return conv_list

    def data_to_product(self, list):
        '''
        Takes a list of dict (product data)
        and returns a list of Product instances.
        '''
        return [product.Product(item) for item in list]


if __name__ == "__main__":
    pr = OpenFoodFactsClient()
    pat = pr.get_data_by_category('pate-a-tartiner', 20)
    print(pr.data_to_product(pat))
