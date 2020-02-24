# -*- coding: utf-8 -*-

import os
import custom_db_manager
import openfoodfacts_client
import menu


class Main():

    def __init__(self):

        self.db = custom_db_manager.CustomDBManager()
        self.menu = menu.Menu()
        if self.db.is_empty:
            self.off_client = openfoodfacts_client.OpenFoodFactsClient()
            self.db.set_database(self.off_client.products)

    def clear_screen(self):
        os.system('cls||clear')

    def choose_in_main_menu(self):
        return self.menu.choose_in_main_menu()

    def find_substitute(self):
        category = self._choose_category()
        product = self._choose_product(category)
        substitute = self._choose_substitute(product)
        self.menu.display_product(substitute)

    def show_substitutions(self):
        # display recorded substitutions and ask user to choose one
        # display information for the selected substitute
        # ask for 0 to go back to main menu
        pass

    def reset_app(self):
        confirmation = input('''ATTENTION :
        Cette opération réinitialisera la base de données.
        Toutes les substitutions enregistrées seront effacées
        de manière IRREVERSIBLE. Voulez-vous continuer ?
        Tapez 'oui' + Entrée pour confirmer,
        ou appuyez sur Entrée pour annuler : ''')

        if confirmation.lower() == 'oui':
            print('Réinitialisation en cours...')
            self.db.empty_database()
            self.off_client = openfoodfacts_client.OpenFoodFactsClient()
            self.db.set_database(self.off_client.products)
            message = ('Réinitialisation terminée')
        else:
            message = ('Opération annulée')

        input(f'{message}. \nAppuyez sur Entrée'
              ' pour revenir au menu principal.')

    def quit_app(self):
        self.db.close_database()
        print('Au revoir !')
        quit()

    def _choose_category(self):
        '''
        Ask user to choose a category of products. Returns category.id.
        '''
        categories = self.db.get_categories()
        categories_list = ['CATEGORIES']
        categories_list.extend([category.name for category in categories])

        cat_index = self.menu.choose_in_list(categories_list)
        id = [category.id for category in categories
              if categories.index(category) == cat_index][0]
        return id

    def _choose_product(self, category):
        # display products and ask user to choose one
        pass

    def _choose_substitute(self, product):
        # display substitutes and ask user to choose one
        pass

    def _save_substitution(self):
        # ask user if they want to record the substitution
        # if yes : save substitution
        pass


if __name__ == '__main__':
    app = Main()

    while True:
        app.clear_screen()
        result = app.choose_in_main_menu()
        if result == 1:
            app.clear_screen()
            app.find_substitute()
            # if user wants to save the substitution:
            # _save_substitution(product, substitute)
        elif result == 2:
            app.show_substitutions()
        elif result == 3:
            app.reset_app()
        elif result == 4:
            app.quit_app()
