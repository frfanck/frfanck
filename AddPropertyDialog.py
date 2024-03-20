import tkinter as tk
from tkinter import ttk

class AddPropertyDialog:
    def __init__(self, parent):
        self.parent = parent
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Add Property")

        # Labels and Entry widgets for property details
        ttk.Label(self.dialog, text="Address:").grid(row=0, column=0, padx=5, pady=5)
        self.address_entry = ttk.Entry(self.dialog)
        self.address_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.dialog, text="Rent Amount:").grid(row=1, column=0, padx=5, pady=5)
        self.rent_entry = ttk.Entry(self.dialog)
        self.rent_entry.grid(row=1, column=1, padx=5, pady=5)

        # Button to add property
        ttk.Button(self.dialog, text="Add Property", command=self.add_property).grid(row=2, columnspan=2, padx=5, pady=5)

    def add_property(self):
        address = self.address_entry.get()
        rent = float(self.rent_entry.get())  # Assuming rent is a numeric value
        # Add logic to add property to database or list
        print("Adding property with address:", address, "and rent:", rent)
        self.dialog.destroy()

# Example usage
root = tk.Tk()
app = AddPropertyDialog(root)
root.mainloop()
