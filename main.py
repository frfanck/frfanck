import tkinter as tk
from tkinter import messagebox
from RentalApplication import RentalApplication

class RentalApplicationGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion Locative")
        self.geometry("600x400")

        # Création de l'application de gestion locative
        self.rental_app = RentalApplication()

        # Ajout des widgets de l'interface utilisateur
        self.create_widgets()

    def create_widgets(self):
        # Titre
        title_label = tk.Label(self, text="Gestion Locative", font=("Helvetica", 18))
        title_label.pack(pady=10)

        # Bouton pour démarrer l'application
        start_button = tk.Button(self, text="Démarrer l'application", command=self.start_application)
        start_button.pack(pady=5)

    def start_application(self):
        # Démarrage de l'application de gestion locative
        self.rental_app.start()
        messagebox.showinfo("Information", "L'application de gestion locative a été fermée.")

if __name__ == "__main__":
    app = RentalApplicationGUI()
    app.mainloop()
