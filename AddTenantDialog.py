import tkinter as tk
from tkinter import ttk

class AddTenantDialog:
    def __init__(self, master):
        self.master = master
        self.master.title("Add Tenant")

        self.frame = ttk.Frame(self.master)
        self.frame.pack(padx=20, pady=20)

        ttk.Label(self.frame, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1)

        ttk.Label(self.frame, text="Contact Info:").grid(row=1, column=0, sticky="w")
        self.contact_entry = ttk.Entry(self.frame)
        self.contact_entry.grid(row=1, column=1)

        self.btn_add = ttk.Button(self.frame, text="Add", command=self.add_tenant)
        self.btn_add.grid(row=2, column=0, columnspan=2, pady=10)

    def add_tenant(self):
        name = self.name_entry.get()
        contact_info = self.contact_entry.get()
        # À implémenter : Ajouter le locataire à la base de données ou à la liste des locataires
        print("Tenant added:", name, contact_info)

def main():
    root = tk.Tk()
    app = AddTenantDialog(root)
    root.mainloop()

if __name__ == "__main__":
    main()
