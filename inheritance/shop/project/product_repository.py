from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            product_object = next(filter(lambda x: x.name == product_name, self.products))

            return product_object

        except StopIteration:
            pass

    def remove(self, product_name):
        try:
            product_object = next(filter(lambda x: x.name == product_name, self.products))

            self.products.remove(product_object)

        except StopIteration:
            pass

    def __repr__(self):
        return '\n'.join(f'{product.name}: {product.quantity}' for product in self.products)
