# -*- coding: utf-8 -*-

import custom_db_manager
import openfoodfacts_client
import menu
import option
import mysql.connector.errors


class Main():

    '''Manages the main app.'''

    def __init__(self):

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
            self.clear_screen()
            result = self.choose_in_main_menu()
            if result == 1:
                self.clear_screen()
                product = self.select_product()
                if product:
                    substitute = self.select_substitute(product)
                    if substitute:
                        substitute.display()
                        self.save_substitution(product, substitute)
            elif result == 2:
                self.display_substitutions()
            elif result == 3:
                self.reset_app()
            elif result == 4:
                quit_app = True
        self.quit_app()

    def clear_screen(self):
        '''Clear screen.'''
        self.menu.clear_screen()

    def choose_in_main_menu(self):
        '''
        Ask the user to select one of the main menu options.
        Return an int according to MAIN_MENU constants.
        '''
        return self.menu.choose_in_main_menu()

    def select_product(self):
        '''
        Ask user to select a category, then a product from this category.
        Return a Product.
        '''
        category = self._select_category()
        if category:
            products_list = self.db.get_products_from_category(category)
            products_set = self.menu.remove_duplicates(products_list)
            products_option = option.Option(
                    f'Produits de la catégorie {category} :', products_set)
            selected_product = self.menu.ask_choice(products_option)
            if selected_product:
                return selected_product

    def select_substitute(self, product):
        '''
        Display a list of products with better nutriscore
         than argument product. Asks user to select one if list is not empty.
         Return selected substitute or None.
        '''
        if product:
            print(f"Recherche d'un substitut (même catégorie) "
                  f"pour le produit {product}")
            substitutes_list = self.db.get_better_nutriscore_products(product)
            if substitutes_list:
                substitutes_option = option.Option(
                    f'Substituts avec un nutriscore meilleur '
                    f'que {product.nutriscore.upper()} :',
                    substitutes_list)
                selected_substitute = self.menu.ask_choice(substitutes_option)
                return selected_substitute
            else:
                print("Il n'existe aucun substitut"
                      " avec un meilleur nutriscore.")
                self._press_enter()
                return None

    def save_substitution(self, product, substitute):
        '''
        Ask user if they want to record substitution and, if yes,
        launch recording.
        '''
        save = ''
        while save.lower() not in ('s', 'm'):
            save = input('\nEntrez S pour sauvegarder la substitution '
                         'ou M pour revenir au menu principal : ')
            if save.lower() == "s":
                self._save_substitution(product, substitute)
            else:
                pass

    def display_substitutions(self):
        '''
        Display recorded substitutions.
        '''

        substitutions = self.db.get_recorded_substitutions()
        if substitutions:
            self.menu.display_substitutions(substitutions)
        else:
            print("Aucune substitution enregistrée.")
        self._press_enter()

    def reset_app(self):
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

    def quit_app(self):
        '''
        Close connector and end program.
        '''
        self.db.close_database()
        print('Au revoir !')
        quit()

    def _select_category(self):
        '''
        Ask user to choose a category of products. Return Category object.
        '''
        categories_options = option.Option('CATEGORIES',
                                           self.db.categories)
        selected_category = self.menu.ask_choice(categories_options)
        return selected_category

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

    def _press_enter(self):
        '''Ask user to press enter to go back to main menu.'''
        input("\nAppuyez sur ENTREE pour revenir au menu principal :")


if __name__ == '__main__':
    app = Main()
    app.start()
