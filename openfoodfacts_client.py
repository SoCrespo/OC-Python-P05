# -*- coding: utf-8 -*-

import requests
from config import URL, API_CATEGORIES, API_TO_PRODUCT_FIELDS, MAX_PRODUCTS_NB
import product


class OpenFoodFactsClient:
    '''
    Retrieves data from openFoodFactAPI and converts them
    in a list of Product objects as instance attribute.
    '''

    def __init__(self):
        self.products = self._get_Products_from_API()

    def _get_data_by_category(self, category, nb):
        '''
        Calls the OpenFoodFact API to retrieve products
        in the given category.

        Downloaded fields are defined in config.py.
        Returns a list of nb dictionaries (1 dict = data of 1 product).

         '''
        payload = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': category,
            'tagtype_1': 'nutrition_grade',
            'tag_contains_1': 'contains',
            'fields': ','.join(API_TO_PRODUCT_FIELDS.keys()),
            'page_size': nb,
            'json': 'true',
        }
        req = requests.get(URL, params=payload)
        return req.json().get('products')

    def _get_data_by_categories(self, categories=API_CATEGORIES,
                                nb=MAX_PRODUCTS_NB):
        '''
        Calls _get_data_by_category() for a list of categories.
        Returns a list of dictionaries (1 dict = data of  1 product)
        Adds the 'category' key in each dict.
        '''
        print("Téléchargement des données en cours...")
        list = []
        for category in categories:
            data = self._get_data_by_category(category, nb)
            for item in data:
                item['category'] = category
            list.extend(data)
        print('Les données ont été correctement récupérées.')
        return list

    def _change_data_keys(self, list):
        '''
        Returns a list of product data (dict) where keys are translated
        into those expected by Product class.
        '''
        conv_list = [{API_TO_PRODUCT_FIELDS[key]: value
                     for key, value in product_data.items()}
                     for product_data in list]
        return conv_list

    def _validate_data(self, dict):
        '''
        Checks if dict data comply with arguments for product.Product().
        Returns a boolean.
        '''
        required_keys = API_TO_PRODUCT_FIELDS.values()
        dict_keys = dict.keys()
        dict_values = dict.values()

        check_nb_keys = len(dict_keys) == len(required_keys)
        check_keys = all([key in dict_keys for key in required_keys])
        check_values = all(dict_values)

        return all((check_nb_keys, check_keys, check_values))

    def _data_to_product(self, list):
        '''
        Takes a list of dict (product data), checks arguments
        and returns a list of Product instances.
        '''
        return [product.Product(data) for data in list
                if self._validate_data(data)]

    def _get_Products_from_API(self):
        '''
        Retrieve data from API, for API_CATEGORIES
        (and for MAX_PRODUCTS_NB products in each category).
        Returns a list of Product objects.
        '''
        data = self._get_data_by_categories()
        conv_data = self._change_data_keys(data)
        products = self._data_to_product(conv_data)
        return products


if __name__ == "__main__":
    pr = OpenFoodFactsClient()
    print([(product.name, product.nutriscore) for product in pr.products])
