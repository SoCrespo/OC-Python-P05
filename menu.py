# -*- coding: utf-8 -*-

import os


class Menu:

    def __init__(self):
        pass

    def ask_choice(self, option):
        '''
        Displays a menu (title and content of Option object)
        and asks user to choose an option.
        Returns the object selected by user or None if 0 is selected.
        '''
        print(f'\n{option.title} \n')
        for index, line in enumerate(option.content, 1):
            print(f'{index} - {line}')

        choice = None

        while choice not in range(0, len(option.content)+1):
            try:
                choice = int(input("\nEntrez le numéro de votre choix "
                                   "ou 0 pour revenir au menu principal : "))
            except ValueError:
                pass
        if choice:
            return option.content[choice - 1]
        else:
            return None

    def choose_in_main_menu(self):
        '''
        Ask the user to select one of the main menu options. Returns an int
        according to MAIN_MENU constant.
        '''
        title = 'MENU PRINCIPAL'

        content = [
                            'Rechercher des substituts à un produit',
                            'Afficher les substitutions enregistrées',
                            'Réinitialisation complète',
                            'Quitter'
                            ]

        print(f'\n{title} \n')
        for index, option in enumerate(content, 1):
            print(f'{index} - {option}')

        choice = None

        while choice not in range(1, len(content)+1):
            try:
                choice = int(input("\nEntrez le numéro de votre choix : "))
            except ValueError:
                pass
        return choice

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

    def get_answer(self):
        pass


if __name__ == "__main__":
    pass
