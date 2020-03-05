# -*- coding: utf-8 -*-


class Category:
    '''
    Represent a category (id in mySQL database, name from API, full name).
    '''

    def __init__(self, id, name, full_name):
        self.id = id
        self.name = name
        self.full_name = full_name

    def __str__(self):
        return self.full_name


if __name__ == "__main__":
    pass
