# -*- coding: utf-8 -*-


class Category:

    def __init__(self, id, name, full_name):
        self.id = id
        self.name = name
        self.full_name = full_name

    def __repr__(self):
        return self.full_name


if __name__ == "__main__":
    pass
