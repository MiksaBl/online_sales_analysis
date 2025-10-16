# product.py
# Klasa za proizvod

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Prikaz informacija o proizvodu
    def show_info(self):
        print(f"Proizvod: {self.name}, Cena: {self.price}, Količina: {self.quantity}")

    # Ažuriranje količine proizvoda
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Količina proizvoda {self.name} ažurirana na {self.quantity}")
