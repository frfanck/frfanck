import tkinter as tk

class RentalManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rental Management System")

        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(padx=20, pady=20)

        self.btn_add_tenant = tk.Button(self.main_frame, text="Add Tenant", command=self.open_add_tenant_dialog)
        self.btn_add_tenant.pack()

    def open_add_tenant_dialog(self):
        # À implémenter : Ouvrir une fenêtre de dialogue pour ajouter un locataire
        pass

def main():
    root = tk.Tk()
    app = RentalManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
