# -*- coding: utf-8 -*-


MAIN_MENU = ['MENU PRINCIPAL',
             'Rechercher des substituts à un produit',
             'Afficher les substitutions enregistrées',
             'Réinitialisation complète',
             'Quitter'
             ]


class Menu:

    def __init__(self):
        pass

    def choose_in_list(self, list):
        '''
        Displays a list (1st item is the title of the list)
        and asks user to choose an option (0 to go back to main menu).
        Returns the number entered by user (int).
        '''
        title = list[0]
        options = list[1:]
        option_indexes = range(1, len(options)+1)

        print(f'\n{title} \n')

        for index, option in zip(option_indexes, options):
            print(f'{index} - {option}')

        choice = None

        while choice not in option_indexes:
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
        choice = self.choose_in_list(MAIN_MENU)
        return choice

    def display_product(self, product):
        product_dict = vars(product)
        for key, value in product_dict:
            print(f'{key}: {value}')


if __name__ == "__main__":
    pass
