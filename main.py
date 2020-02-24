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

    def choose_in_main_menu(self):
        return self.menu.choose_in_main_menu()

    def search_substitute(self):
        print('option 1 en cours de construction')
        # retrieve categories
        # display caterogies and ask user to choose one
        # display products and ask user to choose one
        # display substitutes and ask user to choose one
        # display informations for the selected substitute
        # ask user if they want to record the substitution
        # if yes : record substitution
        # display main menu
        pass

    def show_substitutions(self):
        print('option 2 en cours de construction')
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


if __name__ == '__main__':
    app = Main()

    while True:
        os.system('cls||clear')
        result = app.choose_in_main_menu()
        if result == 1:
            app.search_substitute()
        elif result == 2:
            app.show_substitutions()
        elif result == 3:
            app.reset_app()
        elif result == 4:
            app.quit_app()
