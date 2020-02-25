# -*- coding: utf-8 -*-

import os
import custom_db_manager
import openfoodfacts_client
import menu
import option


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

    def select_product(self):
        category = self._choose_category()
        products_list = self.db.get_products_from_category(category)
        return products_list

    def select_substitute(self, product):
        pass

    def save_substitution(self, product, substitute):
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
        Ask user to choose a category of products. Returns category object.
        '''
        categories = self.db.get_categories()
        categories_options = option.Option('CATEGORIES', categories)

        selected_category_index = self.menu.choose(categories_options)
        selected_category = categories_options.content[
                                        selected_category_index - 1]
        return selected_category


if __name__ == '__main__':
    app = Main()
    quit_app = False
    while not quit_app:
        app.clear_screen()
        result = app.choose_in_main_menu()
        if result == 1:
            app.clear_screen()
            product = app.select_product()
            substitute = app.select_substitute(product)
            # if user wants to save the substitution:
            # _save_substitution(product, substitute)
        elif result == 2:
            app.show_substitutions()
        elif result == 3:
            app.reset_app()
        elif result == 4:
            quit_app = True
    app.quit_app()
