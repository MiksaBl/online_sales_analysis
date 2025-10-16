# main.py
# glavna skripta projekta

from product import Product
from product_manager import ProductManager
from cart import Cart

# kreiranje ProductManager-a
manager = ProductManager()

# dodavanje proizvoda
p1 = Product("Telefon", 50000, 5)
p2 = Product("Televizor", 80000, 2)
p3 = Product("Slusalice", 3000, 10)

manager.dodaj_proizvod(p1)
manager.dodaj_proizvod(p2)
manager.dodaj_proizvod(p3)

# prikaz svih proizvoda
manager.prikazi_proizvode()

# ukupna vrednost
manager.ukupna_vrednost()

# korpa
korpa = Cart()
korpa.dodaj_u_korpu(p1)
korpa.dodaj_u_korpu(p2)
korpa.dodaj_u_korpu(p3)
korpa.prikazi_korpu()
print("Ukupna vrednost korpe:", korpa.ukupna_vrednost(), "RSD")
