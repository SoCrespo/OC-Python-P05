# -*- coding: utf-8 -*-

import os


class Menu:

    def __init__(self):
        pass

    def get_user_choice(self, list_of_choice):
        '''
        Ask user to enter a number corresponding to an item in list_of_choice.
        Return the chosen item or None if user enters "0".
        '''
        self._display_list_of_choice(list_of_choice)
        choice = None
        while choice not in range(0, len(list_of_choice.content)+1):
            try:
                choice = int(input("\nEntrez le numéro de votre choix "
                                   "ou 0 pour revenir au menu principal : "))
            except ValueError:
                pass
        if choice:
            return list_of_choice.content[choice - 1]
        else:
            return None

    def remove_duplicates(self, products_list):
        '''
        Take a list of Products and removes duplicates
        (same brand and name). Returns a list of Products.
        '''
        products_dict = {(item.brand, item.name): item
                         for item in products_list}
        return list(products_dict.values())

    def display_substitutions(self, substitutions_list):
        '''
        Take a list of tuples of Products (origin, substitute)
        and displays each of them.
        '''
        for origin, substitute in substitutions_list:
            print('****************')
            print(f"PRODUIT D'ORIGINE : {origin}")
            print(f"SUBSTITUT : {substitute}")

    def clear_screen(self):
        '''Clear screen.'''
        os.system('cls||clear')

    def _display_list_of_choice(self, list_of_choice):
        '''
        Display a menu (title and content of ListOfChoice object).
        '''
        print(f'\n{list_of_choice.title} \n')
        for index, line in enumerate(list_of_choice.content, 1):
            print(f'{index} - {line}')


if __name__ == "__main__":
    pass
