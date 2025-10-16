# product_manager.py
# Klasa koja upravlja proizvodima

from product import Product

class ProductManager:
    def __init__(self):
        self.products = []  # lista svih proizvoda

    # Dodavanje proizvoda
    def add_product(self, product):
        self.products.append(product)
        print(f"Proizvod {product.name} dodat.")

    # Prikaz svih proizvoda
    def show_products(self):
        if not self.products:
            print("Nema proizvoda u listi.")
            return
        print("Lista proizvoda:")
        for product in self.products:
            print(f"- {product.name}, Cena: {product.price}, Količina: {product.quantity}")

    # Ukupna vrednost svih proizvoda
    def total_value(self):
        ukupno = 0
        for product in self.products:
            ukupno += product.price * product.quantity
        return ukupno

    # Uklanjanje proizvoda po imenu
    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Proizvod {name} uklonjen.")
                return
        print(f"Proizvod {name} nije pronađen.")
