import tkinter as tk

class RentalApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion Locative")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Création des widgets
        label = tk.Label(self, text="Bienvenue dans l'application de gestion locative", font=("Helvetica", 16))
        label.pack(pady=20)

        # Bouton pour gérer les propriétés
        properties_btn = tk.Button(self, text="Gérer les propriétés", command=self.manage_properties)
        properties_btn.pack()
        
        labelFrancois = tk.Label(self, text="Francois BAOULA", bg="orange", fg='white', font=('georgia',45))
        labelFrancois.pack()

        # Bouton pour gérer les locataires
        tenants_btn = tk.Button(self, text="Gérer les locataires", command=self.manage_tenants)
        tenants_btn.pack()

        # Bouton pour gérer les enregistrements de location
        records_btn = tk.Button(self, text="Gérer les enregistrements de location", command=self.manage_records)
        records_btn.pack()

        # Bouton pour gérer les paiements
        payments_btn = tk.Button(self, text="Gérer les paiements", command=self.manage_payments)
        payments_btn.pack()

        # Bouton pour générer des rapports
        reports_btn = tk.Button(self, text="Générer des rapports", command=self.generate_reports)
        reports_btn.pack()

    def manage_properties(self):
        print("Gérer les propriétés")

    def manage_tenants(self):
        print("Gérer les locataires")

    def manage_records(self):
        print("Gérer les enregistrements de location")

    def manage_payments(self):
        print("Gérer les paiements")

    def generate_reports(self):
        print("Générer des rapports")

if __name__ == "__main__":
    app = RentalApplication()
    app.mainloop()
