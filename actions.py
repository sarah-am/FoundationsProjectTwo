# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.mode.com"  # Give your site a name

def welcome():
    print("\nWelcome to %s!\nFeel free to shop throughout the stores we have and only checkout once!" % site_name)

def print_stores():
    for store in stores:
        print(" - " + store.name)

def get_store(store_name):
    # """receives a name for a store, and returns the store object with that name."""
    for store in stores: 
        if store_name == store.name:
            # return store_name.print_products()
            print(store.products)
            # return store.products
            # print(store_name.print_products())
        else:
            return False
    # for store in stores:
    #     return Product.__str__(store)
    # for store in stores:
        # return store.create_product(store, name, description, price)
        # if store == Store("Zara"):
        # return store.__str__().Product()
       # return store_name.print_products(store_name)
    # print my_object.property_name
    # print(str(store.name) + str(store.products))
            # print(store.name + ":" + store.__str__())
            # print(store.print_products)
            # print(str(store.products))
    # picked_store = Store()
    # if picked_store in stores:
    #     return True
        # print store.Product(picked_store)
        # return True and print(picked_store.__str__)
    # return store_name.print_products(store.name)
    

def pick_store():
    # """prints list of stores and prompts user to pick a store."""
    print_stores()
    print("Pick a store by typing its name. Once done, type \"checkout\" to pay your bills and leave.")       
    while True:
        store = str(input(" > "))
        for store in stores:
            if store == store.name:
                return get_store(store)
            elif store == "checkout":
                return store.checkout()
            else:
                print("No store with that name. Please try again.")
                break
        # if type(get_store(picked_store)) == True:
        #     return get_store(picked_store)
            # new_emp_1 = Employee.from_string(emp_str_1)
            # print(Product.__str__(name,description,price))   
        # if picked_store in stores:
        #     return get_store()
        # elif picked_store == "checkout":
        #     return Cart.checkout()

def pick_products(cart, picked_store):
    # """prints list of products and prompts user to add products to cart."""
    # get_store(picked_store)
    cart.print_products()
    print("What would you like to purchase? Please type the exact name of the product.")
    chosen_product = str(input(" > "))
    if chosen_product in picked_store:
        cart.append(chosen_product)
    elif chosen_product not in picked_store:
        print("Not valid entry. Please try again.")
    elif chosen_product == "back":
        pick_store()

def shop():
    # """The main shopping functionality"""
    cart = Cart()
    pick_store()
    # get_store()
    picked_store = store.name
    pick_products(cart, picked_store)
    cart.print_receipt()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
