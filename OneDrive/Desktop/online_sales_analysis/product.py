# product.py
# klasa za proizvode

class Product:
    def __init__(self, name, price, quantity):
        # atributi proizvoda
        self.name = name
        self.price = price
        self.quantity = quantity

    def prikazi_info(self):
        # ispis informacija o proizvodu
        print(f"Naziv: {self.name}, Cena: {self.price} RSD, Kolicina: {self.quantity}")

    def azuriraj_kolicinu(self, nova_kolicina):
        # menjanje kolicine proizvoda
        self.quantity = nova_kolicina
        print(f"Kolicina proizvoda '{self.name}' je azurirana na {self.quantity}.")
