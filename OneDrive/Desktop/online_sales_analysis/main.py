# main.py
# Testiranje ProductManager i Cart funkcionalnosti

from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Laptop", 1000, 2))
manager.add_product(Product("Miš", 20, 5))
manager.add_product(Product("Tastatura", 50, 3))
manager.add_product(Product("Monitor", 150, 1))
manager.add_product(Product("USB kabl", 5, 10))

# Prikaz svih proizvoda
manager.show_products()

# Prikaz ukupne vrednosti inventara
print(f"Ukupna vrednost svih proizvoda: {manager.total_value()}")

# Test uklanjanja proizvoda
manager.remove_product("Miš")
manager.show_products()
print(f"Ukupna vrednost svih proizvoda: {manager.total_value()}")

# --------------------------
# Deo za Cart funkcionalnost
# --------------------------
korpa = Cart()  # kreiranje instance Cart

# Dodavanje 3 proizvoda iz ProductManager liste u korpu
korpa.add_to_cart(manager.products[0])
korpa.add_to_cart(manager.products[1])
korpa.add_to_cart(manager.products[2])

# Prikaz sadržaja korpe
korpa.show_cart()

# Prikaz ukupne vrednosti korpe
print(f"Ukupna vrednost za naplatu: {korpa.total_price()}")
