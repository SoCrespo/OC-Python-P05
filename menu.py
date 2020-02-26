# -*- coding: utf-8 -*-
import constants


MAIN_MENU_TITLE = constants.MAIN_MENU_TITLE
MAIN_MENU_CONTENT = constants.MAIN_MENU_CONTENT


class Menu:

    def __init__(self):
        pass

    def choose(self, option):
        '''
        Displays a menu (title and content of Option object)
        and asks user to choose an option.
        Returns the object selected by user.
        '''
        # content = option.content

        print(f'\n{option.title} \n')
        for index, line in enumerate(option.content, 1):
            print(f'{index} - {line}')

        choice = None

        while choice not in range(1, len(option.content)+1):
            try:
                choice = int(input("\nEntrez le numéro de votre choix : "))
            except ValueError:
                pass
        return option.content[choice - 1]

    def choose_in_main_menu(self):
        '''
        Ask the user to select one of the main menu options. Returns an int
        according to MAIN_MENU constant.
        '''
        print(f'\n{MAIN_MENU_TITLE} \n')
        for index, option in enumerate(MAIN_MENU_CONTENT, 1):
            print(f'{index} - {option}')

        choice = None

        while choice not in range(1, len(MAIN_MENU_CONTENT)+1):
            try:
                choice = int(input("\nEntrez le numéro de votre choix : "))
            except ValueError:
                pass
        return choice

    def remove_duplicates(self, products_list):
        '''Takes a list of Products and removes duplicates
        (same brand and name). Returns a list of Products. '''
        products_dict = {(item.brand, item.name): item
                         for item in products_list}
        return list(products_dict.values())


if __name__ == "__main__":
    pass
