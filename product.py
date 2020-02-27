# -*- coding: utf-8 -*-

from constants import PRODUCT_ATTRIBUTES


class Product:

    def __init__(self, dict):
        self.category = dict['category']
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

    def __repr__(self):
        return f'{self.brand} - {self.name} - nutriscore : {self.nutriscore}'

    def convert_category_to_cat_id(self, categories):
        '''Sets product.cat_id according to product.category,
        then deletes product.category.'''
        for cat in categories:
            if self.category == cat.name:
                self.cat_id = cat.id
        del(self.category)

    def convert_cat_id_to_category(self, categories):
        '''Sets product.category according to product.cat_id,
        then deletes product.cat_id.'''
        for cat in categories:
            if self.cat_id == cat.id:
                self.category = cat.category
        del(self.cat_id)

    def display(self):
        for key, value in vars(self).items():
            if key not in ('id', 'category'):
                print(f'{PRODUCT_ATTRIBUTES[key]} : {value}')


if __name__ == "__main__":
    pass
