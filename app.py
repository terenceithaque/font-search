from tkinter import *
import requests

# Adresse de l'API Google Fonts
url = "https/www.googleapis.com/webfonts/v1/webfonts"


class Application(Tk):
    "Application"

    def __init__(self):
        super().__init__()
        # Demander à l'utilisateur de saisir une police d'écriture
        self.label_recherche = Label(
            self, text="Saisissez une police d'écriture:")
        self.label_recherche.pack()
        # Champ de texte pour permettre à l'utilisateur d'effectuer sa recherche
        self.barre_recherche = Entry(self)
        # Faire s'étendre la barre de recherche sur toute la longueur de la fenêtre
        self.barre_recherche.pack(fill="x")


app = Application()  # Application
app.mainloop()  # Démarrer l'application
