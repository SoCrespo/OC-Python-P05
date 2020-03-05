# -*- coding: utf-8 -*-

from constants import PRODUCT_ATTRIBUTES


class Product:
    '''
    Represent a product and its data (brand, name, full name, nutriscore...
    Used to convey data from API call, and to retrieve from / insert into
    custom 'product' database.
    '''

    def __init__(self, dict):
        self.brand = dict['brand']
        self.name = dict['name']
        self.full_name = dict['full_name']
        self.quantity = dict['quantity']
        self.nutriscore = dict['nutriscore'].upper()
        self.url = dict['url']
        self.ingredients = dict['ingredients']
        self.stores = dict['stores']
        if 'id' in dict.keys():
            self.id = dict['id']
        if'category' in dict.keys():
            self.category = dict['category']

    def __repr__(self):
        return f'{self.brand} - {self.name} - nutriscore : {self.nutriscore}'

    def convert_category_to_cat_id(self, categories):
        '''
        Set product.cat_id according to product.category,
        then deletes product.category. Used to insert product
        in MySQL database with required fields.
        '''
        for cat in categories:
            if self.category == cat.name:
                self.cat_id = cat.id
        del(self.category)

    def display(self):
        '''
        Display all data of product in a human-readable way.
        '''
        for key, value in vars(self).items():
            if key not in ('id', 'category'):
                print(f'{PRODUCT_ATTRIBUTES[key]} : {value}')


if __name__ == "__main__":
    pass
