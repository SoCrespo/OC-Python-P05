# -*- coding: utf-8 -*-


class Product:

    def __init__(self, dict):
        self.category = dict['category']
        self.brand = dict['brand']
        self.name = dict['name']
        self.full_name = dict['full_name']
        self.quantity = dict['quantity']
        self.nutriscore = dict['nutriscore']
        self.url = dict['url']
        self.ingredients = dict['ingredients']
        self.stores = dict['stores']


if __name__ == "__main__":
    pass
