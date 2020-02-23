# -*- coding: utf-8 -*-


class Menu:

    def __init__(self):
        pass

    def choose_in_main_menu(self):
        '''
        Asks user to choose among 4 options:
        - search a product
        - access saved previous searches
        - reset database
        - quit
        returns user's option (int between 1 and 4).
        '''

        options_text = '''
        Choisissez parmi les options suivantes :

        1 - Rechercher des substituts à un produit
        2 - Afficher les substitutions enregistrées
        3 - Réinitialiser la base de données (supprimera vos enregistrements)
        4 - Quitter

        '''
        print(options_text)
        option = None
        while option not in [1, 2, 3, 4]:
            try:
                option = int(input("Votre choix (1, 2, 3 ou 4) : "))
            except ValueError:
                pass

        options_dict = {
            1: self.select_category,
            2: self.show_substitutes,
            3: self.reset_database,
            4: self.quit_app
        }
        return options_dict[option]

    def select_category(self):
        '''
        Displays categories and aaks user to select one.
        '''
        print('fonction select_category')

    def select_product(self, list):
        '''
        Asks user to choose a product in a given list.
        '''
        pass

    def show_substitutes(self, product):
        '''
        Displays a list of healthier substitutes (better nutriscore index)
        for the selected product.
        '''
        # provide answer if no healthier substitute can be found.
        print('fonction show_substitute')

    def display_product(self, product):
        '''
        Displays all fields of a product
        (name, nutriscore, ingredients, url...)
        '''
        pass

    def save_substitution(self, product, substitute):
        '''
        Records substitute for a product.
        '''
        pass

    def reset_database(self):
        '''Drops all tables of database and recreates the list of products.
        CAUTION : deletes also all recorded substitutions !
        '''
        # provide double validation and warning
        # for recorded substitutions deletion.
        print('fonction reset_database')

    def quit_app(self):
        '''Closes DB and quits app.'''
        print('fonction quit_app')


if __name__ == "__main__":
    pass
