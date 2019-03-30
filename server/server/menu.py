from collections import namedtuple
from products.models import Product, ProductCategory


categories = ProductCategory.objects.all()
products = Product.objects.all()
Menu = namedtuple('Menu', 'name, id')
Menu = [Menu(itm.name, itm.id) for itm in categories]