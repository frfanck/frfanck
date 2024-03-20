class RentalRecord:
    def __init__(self, property, tenant, lease_term, rent_paid):
        self.property = property
        self.tenant = tenant
        self.lease_term = lease_term
        self.rent_paid = rent_paid
def manage_rental_records(self):
    print("Rental record management:")
    # Afficher la liste des enregistrements de location existants
    for record in self.rental_records:
        print(record)
    # Ajouter un nouvel enregistrement de location
    # Assurez-vous de lier une propriété et un locataire existants à cet enregistrement
    # Demandez les détails du bail (durée, montant du loyer, etc.)
    # Ajoutez l'enregistrement à la liste des enregistrements de location
    print("Rental record added successfully.")

    def __str__(self):
        return f"Rental Record:\nProperty: {self.property}\nTenant: {self.tenant}\nLease Term: {self.lease_term}\nRent Paid: {self.rent_paid}"
