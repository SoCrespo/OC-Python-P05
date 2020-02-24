# -*- coding: utf-8 -*-
import constants
import option

MAIN_MENU_TITLE = constants.MAIN_MENU_TITLE
MAIN_MENU_CONTENT = constants.MAIN_MENU_CONTENT


class Menu:

    def __init__(self):
        self.main_menu_options = option.Option(MAIN_MENU_TITLE,
                                               MAIN_MENU_CONTENT)

    def choose(self, option):
        '''
        Displays a menu (title and content of Option object)
        and asks user to choose an option.
        Returns the number entered by user (int).
        '''
        title = option.title
        content = option.content

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

    def choose_in_main_menu(self):
        '''
        Ask the user to select one of the main menu options. Returns an int
        according to MAIN_MENU constant.
        '''
        return self.choose(self.main_menu_options)

    def display_product(self, product):
        product_dict = vars(product)
        for key, value in product_dict:
            print(f'{key}: {value}')


if __name__ == "__main__":
    pass
