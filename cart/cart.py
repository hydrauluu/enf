"""Сессионная корзина, хранящая товары в сессии.
Была закоментированна, так как есть другая реализация"""

# from decimal import Decimal

# from django.shortcuts import get_object_or_404

# from main.models import Product


# class Cart:
#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get("cart")
#         if not cart:
#             cart = self.session["cart"] = {}
#         self.cart = cart

#     def add(self, product, size, quantity=1, override_quantity=False):
#         product_id = str(product.id)
#         size_name = str(size)

#         cart_key = f"{product_id}_{size_name}"

#         if cart_key not in self.cart:
#             self.cart[cart_key] = {
#                 "size": size_name,
#                 "quantity": 0,
#                 "price": str(product.price),
#                 "product_id": product_id,
#             }

#         if override_quantity:
#             self.cart[cart_key]["quantity"] = override_quantity
#         else:
#             self.cart[cart_key]["quantity"] += quantity

#         self.save()

#     def remove(self, product, size):
#         product_id = str(product.id)
#         size_name = str(size)
#         cart_key = f"{product_id}_{size_name}"

#         if cart_key in self.cart:
#             del self.cart[cart_key]
#             self.save()

#     def save(self):
#         self.session["cart"] = self.cart
#         self.session.modified = True

#     def update_quantity(self, product, size, quantity):
#         if quantity <= 0:
#             self.remove(product, size)
#         else:
#             self.add(product, size, quantity, override_quantity=True)

#     def __iter__(self):
#         product_ids = [item["product_id"] for item in self.cart.values()]
#         products = Product.objects.filter(id__in=product_ids)
#         cart = self.cart.copy()

#         for product in products:
#             for cart_key, cart_item in cart.items():
#                 if cart_key["product_id" == str(product_ids)]:
#                     cart_item["product"] = product
#                     cart_item["total_price"] = (
#                         Decimal(cart_item["price"]) * cart_item["quantity"]
#                     )
#                     yield cart_item

#     def __len__(self):
#         lenght = sum(item["quantity"] for item in self.cart.values())
#         return lenght

#     def get_total_price(self):
#         total_price = sum(
#             Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
#         )
#         return total_price

#     def clear(self):
#         del self.session["cart"]
#         self.save()

#     def get_cart_items(self):
#         items = []
#         for item in self:
#             items.append(
#                 {
#                     "product": item["product"],
#                     "size": item["size"],
#                     "quantity": item["quantity"],
#                     "price": Decimal(item["price"]),
#                     "total_price": item["total_price"],
#                     "cart_key": f"{item['product_id']}_{item['size']}",
#                 }
#             )
#         return items
