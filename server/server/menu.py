from collections import namedtuple
from products.models import Product, ProductCategory


categories = ProductCategory.objects.all()
products = Product.objects.all()
Cat = namedtuple('Cat', 'name, id')
Prod = namedtuple('Prod', 'name, id, category_id')
menu_categories = [Cat(itm.name, itm.id) for itm in categories]
menu_products = [Prod(itm.name, itm.id, itm.category_id) for itm in products]
