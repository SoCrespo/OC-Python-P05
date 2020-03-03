# -*- coding: utf-8 -*-

import custom_db_manager
import openfoodfacts_client
import menu
import list_of_choice
import mysql.connector.errors


class Main():

    '''Manage the main app.'''

    def __init__(self):
        '''Instanciate CustomDBManager and Menu objects. If MySQL database
        is empty, instanciate OpenFoodFactsClient to retrieve data, then
        fill database.'''

        self.db = custom_db_manager.CustomDBManager()
        self.menu = menu.Menu()
        if self.db.is_empty:
            self.off_client = openfoodfacts_client.OpenFoodFactsClient()
            self.db.reset_database(self.off_client.products)

    def start(self):
        '''
        Main loop of the program.
        '''
        quit_app = False
        while not quit_app:
            self._clear_screen()
            user_choice = self._choose_in_main_menu()
            if user_choice == 1:  # Find a substitute
                self._clear_screen()
                product = self._select_product()
                if product:
                    print(f"\nRecherche d'un substitut à {product}")
                    substitutes = self._get_substitutes(product)
                    selected_substitute = self._select_substitute(substitutes)
                    if selected_substitute:
                        selected_substitute.display()
                        if self._ask_for_recording():
                            self._save_substitution(
                                product, selected_substitute
                                )
            elif user_choice == 2:  # Display recorded substitutes
                self._display_substitutions()
            elif user_choice == 3:  # Reset database
                self._reset_app()
            elif user_choice == 4:  # Quit app
                quit_app = True
        self._quit_app()

    def _clear_screen(self):
        '''Clear screen.'''
        self.menu.clear_screen()

    def _choose_in_main_menu(self):
        '''
        Ask the user to select one of the main menu options.
        '''
        return self.menu.choose_in_main_menu()

    def _select_category(self):
        '''
        Ask user to choose a category of products. Return Category object.
        '''
        category_list_of_choice = (
            list_of_choice.ListOfChoice('CATEGORIES', self.db.categories)
        )
        selected_category = self.menu.get_user_choice(category_list_of_choice)
        return selected_category

    def _select_product(self):
        '''
        Ask user to select a category, then a product from this category.
        Return a Product or None.
        '''
        category = self._select_category()
        if category:
            products_list = self.db.get_products_from_category(category)
            products_set = self.menu.remove_duplicates(products_list)
            products_list_of_choice = list_of_choice.ListOfChoice(
                    f'Produits de la catégorie {category} :', products_set)
            selected_product = (
                self.menu.get_user_choice(products_list_of_choice)
                )
            if selected_product:
                return selected_product

    def _get_substitutes(self, product):
        '''Retrieve from custom database a list of products with a better
        nutriscore than argument product.
        Return a list of Products (that may be empty).
        '''
        return self.db.get_better_nutriscore_products(product)

    def _select_substitute(self, substitutes_list):
        '''
        Display a list of products with better nutriscore
        than argument product. Ask user to select one if list is not empty.
        Return selected substitute, or None if list is empty.
        '''
        # print(f"Recherche d'un substitut (même catégorie) "
        #      f"pour le produit {product}")
        if substitutes_list:
            substitutes_list_of_choice = list_of_choice.ListOfChoice(
                f'Substituts disponibles :', substitutes_list)
            substitutes_list_of_choice.sort_by_nutriscore()
            selected_substitute = (
                self.menu.get_user_choice(substitutes_list_of_choice)
            )
            return selected_substitute
        else:
            print("Il n'existe aucun substitut"
                  " avec un meilleur nutriscore.")
            self._press_enter()
            return None

    def _display_substitutions(self):
        '''
        Display recorded substitutions.
        '''

        substitutions = self.db.get_recorded_substitutions()
        if substitutions:
            self.menu.display_substitutions(substitutions)
        else:
            print("Aucune substitution enregistrée.")
        self._press_enter()

    def _ask_for_recording(self):
        '''
        Ask user if they want to record substitution. Return boolean.
        '''
        save = ''
        save = input('\nEntrez S pour sauvegarder la substitution '
                     'ou faites Entrée pour revenir au menu principal : ')
        return save.lower() == "s"

    def _save_substitution(self, origin, substitute):
        '''
        Insert a pair of products (origin and substitute)
        in substitution table.
        '''
        try:
            self.db.save_substitution(origin, substitute)
        except mysql.connector.errors.IntegrityError:
            print("L'enregistrement existe déjà.")
        else:
            print(
                f"La substitution du produit {origin.brand} - {origin.name} "
                f"par {substitute.brand} - {substitute.name} a bien été "
                f"enregistrée."
            )
        finally:
            self._press_enter()

    def _reset_app(self):
        '''
        Drop all existing tables in the database, recreate them
        and fill them with data from API.
        '''

        warning = ("\nATTENTION : Cette opération réinitialisera "
                   "la base de données.\nToutes les substitutions "
                   "enregistrées seront DEFINITIVEMENT effacées. "
                   "\nVoulez-vous continuer ?\n"
                   "Tapez 'oui' + Entrée pour confirmer, ou "
                   "appuyez sur Entrée pour annuler : ")
        confirmation = input(warning)
        if confirmation.lower() == 'oui':
            print('Réinitialisation en cours...')
            self.db.empty_database()
            self.off_client = openfoodfacts_client.OpenFoodFactsClient()
            self.db.reset_database(self.off_client.products)
            message = ('Réinitialisation terminée.')
        else:
            message = ('Opération annulée.')
        print(message)
        self._press_enter()

    def _quit_app(self):
        '''
        Close connector and end program.
        '''
        self.db.close_database()
        print('Au revoir !')
        quit()

    def _press_enter(self):
        '''Ask user to press enter to go back to main menu.'''
        input("\nAppuyez sur ENTREE pour revenir au menu principal :")


if __name__ == '__main__':
    app = Main()
    app.start()
