class Property:
    def __init__(self, address, rent_amount):
        self.address = address
        self.rent_amount = rent_amount
def manage_properties(self):
    print("Property management:")
    # Afficher la liste des propriétés existantes
    for property in self.properties:
        print(property)
    # Ajouter une nouvelle propriété
    address = input("Enter property address: ")
    rent_amount = float(input("Enter rent amount: "))
    new_property = Property(address, rent_amount)
    self.properties.append(new_property)
    print("Property added successfully.")

    def __str__(self):
        return f"Property at {self.address}, Rent: {self.rent_amount}"
