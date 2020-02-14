# -*- coding: utf-8 -*-

import requests
import config as cf
import product


class OpenFoodFactsClient:
    '''
    Retrieves data from openFoodFactAPI and converts them
    in a list of Product objects.
    '''

    def __init__(self):
        pass

    def get_data_by_category(self, category, nb):
        '''
        Calls the OpenFoodFact API to retrieve products
        in the given category.

        Downloaded fields are defined in config.py.
        Returns a list of nb dictionaries (1 dict = data of 1 product).

         '''
        url = cf.URL
        payload = cf.payload_for(category, nb)
        req = requests.get(url, params=payload)
        return req.json().get('products')

    def get_data_by_categories(self, categories, nb):
        '''
        Calls get_data_by_category() for a list of categories.
        Returns a list of dictionaries (1 dict = data of  1 product)
        Adds the 'category' key in each dict.
        '''
        print("Retrieving data, please wait...")
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
        tags = cf.API_TO_PRODUCT_FIELDS
        conv_list = [{tags[key]: value for key, value in product_data.items()}
                     for product_data in list]
        return conv_list

    def validate_data(self, dict):
        '''
        Checks if dict data comply with arguments for product.Product().
        Returns a boolean.
        '''
        required_keys = cf.API_TO_PRODUCT_FIELDS.values()
        dict_keys = dict.keys()
        dict_values = dict.values()

        check_nb_keys = len(dict_keys) == len(required_keys)
        check_keys = all([key in dict_keys for key in required_keys])
        check_values = all(dict_values)

        return all((check_nb_keys, check_keys, check_values))

    def data_to_product(self, list):
        '''
        Takes a list of dict (product data), checks arguments
        and returns a list of Product instances.
        '''
        return [product.Product(data) for data in list
                if self.validate_data(data)]


if __name__ == "__main__":
    pr = OpenFoodFactsClient()
    pat = pr.get_data_by_categories(['pate-a-tartiner'], 50)
    conv_pat = pr.change_data_keys(pat)
    products = pr.data_to_product(conv_pat)
    print([product.nutriscore for product in products])
