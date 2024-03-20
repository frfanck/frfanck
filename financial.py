class Financial:
    @staticmethod
    def calculate_income(rental_records):
        total_income = sum(record.property.rent_amount for record in rental_records)
        return total_income

    @staticmethod
    def calculate_expenses(rental_records):
        total_expenses = 0  # Ajoutez ici le calcul des dépenses
        return total_expenses

    @staticmethod
    def calculate_profit(income, expenses):
        return income - expenses
def manage_payments(self):
    print("Payment management:")
    # Afficher la liste des paiements en attente
    for payment in self.pending_payments:
        print(payment)
    # Enregistrer un nouveau paiement
    # Demandez les détails du paiement (montant, date, locataire concerné, etc.)
    # Mettez à jour le statut du paiement
    print("Payment recorded successfully.")
