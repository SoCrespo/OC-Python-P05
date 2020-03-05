# -*- coding: utf-8 -*-


class ListOfChoice:

    '''Group a list of items (ListOfChoice.content)
    and the title of this list (ListOfChoice.list).
    Used by Menu class to display a menu of variable length.'''

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def sort_by_brand_and_name(self):
        '''
        Sort self.content (list of products) by product.brand and .name,
        case-insensitively.
        '''
        self.content.sort(key=lambda prod: (
                    getattr(prod, 'brand').lower(),
                    getattr(prod, 'name').lower()
                )
        )

    def sort_by_nutriscore(self):
        '''
        Sort self.content (list of products) by product.nutriscore.
        '''
        self.content.sort(key=lambda prod: prod.nutriscore)


if __name__ == "__main__":
    pass
