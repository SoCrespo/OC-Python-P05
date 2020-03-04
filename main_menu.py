# -*- coding: utf-8 -*-


class MainMenu:
    '''
    Manages app's main menu.
    '''

    FIND_AND_RECORD_SUBSTITUTE = 'Rechercher des substituts à un produit'
    DISPLAY_SUBSTITUTIONS = 'Afficher les substitutions enregistrées'
    RESET = 'Réinitialisation complète'
    QUIT = 'Quitter'

    def __init__(self):
        self.title = "MENU PRINCIPAL\n"
        self.options = {
                        1: self.FIND_AND_RECORD_SUBSTITUTE,
                        2: self.DISPLAY_SUBSTITUTIONS,
                        3: self.RESET,
                        4: self.QUIT
                    }

    def display(self):
        '''
        Display main menu.
        '''
        print(self.title)
        for index, option in self.options.items():
            print(f'{index} - {option}')

    def get_choice(self):
        '''
        Return user's choice (a constant among MainMenu attributes)
        in main menu.
        '''
        choice = ''
        while choice not in self.options.keys():
            try:
                choice = int(input("\nEntrez le numéro de votre choix : "))
            except ValueError:
                pass
        return self.options[choice]


if __name__ == "__main__":
    pass
