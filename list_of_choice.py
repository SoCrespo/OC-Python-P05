# -*- coding: utf-8 -*-


class ListOfChoice:

    '''Group a list of items (ListOfChoice.content)
    and the title of this list (ListOfChoice.list).
    Used by Menu class.'''

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def sort_by_brand(self):
        self.content.sort(key=lambda prod: prod.brand)

    def sort_by_nutriscore(self):
        self.content.sort(key=lambda prod: prod.nutriscore)


if __name__ == "__main__":
    pass
