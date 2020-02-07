# -*- coding: utf-8 -*-

import config as cf


class Product:

    def valid_data(self, dict):
        required_keys = cf.CONVERTING_FIELDS.values()
        dict_keys = dict.keys()
        dict_values = dict.values()

        check_nb_keys = len(dict_keys) == len(required_keys)
        check_keys = all([key in dict_keys for key in required_keys])
        check_values = all(dict_values)

        print(f'nb keys: {check_nb_keys}, check keys: {check_keys}, check values: {check_values}, ALL: {all((check_nb_keys, check_keys, check_values))}')
        return all((check_nb_keys, check_keys, check_values))

    def __init__(self, dict):
        if self.valid_data(dict):
            self.category = dict['category']
            self.brand = dict['brand']
            self.name = dict['name']
            self.full_name = dict['full_name']
            self.quantity = dict['quantity']
            self.nutriscore = dict['nutriscore']
            self.url = dict['url']
            self.ingredients = dict['ingredients']
            self.stores = dict['stores']
        else:
            print('données non conformes')    

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    pass
