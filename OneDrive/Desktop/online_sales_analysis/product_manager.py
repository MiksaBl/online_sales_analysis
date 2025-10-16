# product_manager.py
# upravljanje proizvodima

from product import Product

class ProductManager:
    def __init__(self):
        # lista proizvoda
        self.proizvodi = []

    def dodaj_proizvod(self, product):
        # dodavanje proizvoda u listu
        self.proizvodi.append(product)

    def prikazi_proizvode(self):
        # ispis svih proizvoda
        if len(self.proizvodi) == 0:
            print("Nema proizvoda.")
        else:
            for p in self.proizvodi:
                p.prikazi_info()

    def ukupna_vrednost(self):
        # racunanje ukupne vrednosti svih proizvoda
        total = 0
        for p in self.proizvodi:
            total += p.price * p.quantity
        print(f"Ukupna vrednost svih proizvoda: {total} RSD")

    def ukloni_proizvod(self, naziv):
        # brisanje proizvoda po imenu
        for p in self.proizvodi:
            if p.name == naziv:
                self.proizvodi.remove(p)
                print(f"Proizvod '{naziv}' je uklonjen.")
                return
        print(f"Proizvod '{naziv}' nije pronadjen.")
