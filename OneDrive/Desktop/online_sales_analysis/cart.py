# cart.py
# Klasa koja upravlja korpom kupca

class Cart:
    def __init__(self):
        self.cart_items = []  # lista proizvoda u korpi

    # Dodavanje proizvoda u korpu
    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Proizvod {product.name} dodat u korpu.")

    # Računanje ukupne vrednosti korpe
    def total_price(self):
        ukupno = 0
        for item in self.cart_items:
            ukupno += item.price * item.quantity
        return ukupno

    # Prikaz sadržaja korpe
    def show_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
            return
        print("Sadržaj korpe:")
        for item in self.cart_items:
            print(f"- {item.name}, Cena: {item.price}, Količina: {item.quantity}")
