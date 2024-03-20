class Tenant:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
def manage_tenants(self):
    print("Tenant management:")
    # Afficher la liste des locataires existants
    for tenant in self.tenants:
        print(tenant)
    # Ajouter un nouveau locataire
    name = input("Enter tenant name: ")
    contact_info = input("Enter contact information: ")
    new_tenant = Tenant(name, contact_info)
    self.tenants.append(new_tenant)
    print("Tenant added successfully.")

    def __str__(self):
        return f"Tenant: {self.name}, Contact: {self.contact_info}"
