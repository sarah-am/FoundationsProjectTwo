# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def print_products(self):
        print(self.products)
        # print(" - " + self.products)

class Product():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return self.name + self.description + self.price
        # print(self.name, self.description, self.price)
        # print(self.name + self.description + self.price)
        # print("""Product Name: {}
        #           Description: {}
        #           Price: {}KD""".format(self.name, self.description, self.price))
        # return str(self.__class__) + ": " + str(self.__dict__)
        # return "{} , {} , {}".format(self.name, self.description, self.price)
        # store_products = Product(product.name, product.description, product.price)

class Cart():
    def __init__(self):
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def get_total_price(self):
        total = 0
        for product in product: 
            if product in self.products:
                total += self.products[product]
        return total
        # int.__add__(self.products)
        # self.price + other.price
        # total = sum(self.products)

    def print_receipt(self):
        print("Here is your receipt: " + self.products + self.get_total_price())

    def checkout(self):
        self.print_receipt()
        print("Do you confirm? yes/no")
        answer = str(input(" > "))
        if answer == "yes" or "y":
            return self.get_total_price() + print("Your order has been placed.")
        elif answer == "no" or "n":
            print("Your order has been cancelled.")
        # if "yes":
        #     print("Your order has been placed.")
        # elif "no":
        #     print("Your order has been cancelled")
        # print("Confirm? yes/no") + str(input)