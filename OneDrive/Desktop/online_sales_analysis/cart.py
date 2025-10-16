# cart.py
# klasa za korpu kupca

class Cart:
    def __init__(self):
        # lista proizvoda u korpi
        self.cart_items = []

    def dodaj_u_korpu(self, product):
        self.cart_items.append(product)
        print(f"Dodat u korpu: {product.name}")

    def ukupna_vrednost(self):
        total = 0
        for p in self.cart_items:
            total += p.price * p.quantity
        return total

    def prikazi_korpu(self):
        print("Sadrzaj korpe:")
        for p in self.cart_items:
            print(f"- {p.name}, {p.price} RSD x {p.quantity}")
