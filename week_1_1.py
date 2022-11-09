"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):

        self.total_items = []
        self.total_price = 0
        self.discount = 0
        self.total_items_details = []

    def add_item(self, item, price):

        # Adding item details dict to list.
        # If that item has already been bought. i.e.,
        # the customer is buying multiple of the same item,
        # instead, increase the number bought by one and the price by one unit
        # rather than having duplicates in the total_items_details list.
        # I have kept duplicates in total_items.

        if item not in self.total_items:
            new_item = {
                'item': item,
                'no.': 1,
                'price': price}
            self.total_items_details.append(new_item)
        elif item in self.total_items:
            for i in self.total_items_details:
                if i['item'] == item:
                    i['no.'] += 1
                    i['price'] += price

        self.total_items.append(item)
        self.total_price += price

    def remove_item(self, item):

        # Removing the one instance of the item from total_items_details
        # if it indeed has already been 'checked out'.
        # Removes the total price of that item from the total price.
        # Removes all instances of the item from total_items.

        if item in self.total_items:
            for i in self.total_items_details:
                if i['item'] == item:
                    self.total_price -= i['price']
                    self.total_items_details.remove(i)

        while item in self.total_items:
            self.total_items.remove(item)

    def set_discount(self, discount):
        self.discount = discount

    def apply_discount(self):

        # Changes all prices in self_items_details to the discount price and
        # applies the discount to the whole of the total_price.
        # And prints confirmation message.

        for i in self.total_items_details:
            i['price'] -= i['price'] * (self.discount/100)

        self.total_price -= self.total_price * (self.discount/100)

        print(f"A {self.discount}% discount has been applied.")

    def get_total(self):
        # Prints total price, rounds it to two decimal points.

        print("Total: " + str(round(self.total_price, 2)))

    def show_items(self):
        # Prints item list.
        print("Items: " + str(self.total_items))

    def show_all(self):
        # Creates a copy of the dictionary, so that the rounding will not affect the 'raw' data.
        # Rounds price to two decimal points before printing.
        # Prints each items' details in a different line with the number position.

        total_details = self.total_items_details.copy()
        for i in range(len(total_details)):
            round(total_details[i]['price'], 2)
            print(str(i+1) + " " + str(total_details[i]))

    def reset_register(self):
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0
        self.total_items_details.clear()
        pass


# EXAMPLE code run:
cash_reg = CashRegister()

# Checking out some bread and a croissant (yum!)
cash_reg.add_item('bread', 4.0)
cash_reg.add_item('croissant', 3.0)
cash_reg.add_item('bread', 4.0)

# Total adds up to 13, items are shown (inc. duplicates)
# but no duplicates in dict list (and 2 units of bread instead shown, with price doubled to 8.0)
print("Example checkout")
cash_reg.show_items()
cash_reg.get_total()
cash_reg.show_all()

# Applying discount with default 0, then set discount to 20% and apply again.
print("\nExample discount")
cash_reg.apply_discount()
cash_reg.show_items()
cash_reg.get_total()
cash_reg.show_all()
cash_reg.set_discount(20)
cash_reg.apply_discount()

# Checking that total price changed and also that each individual price in the dict list has changed.
cash_reg.show_items()
cash_reg.get_total()
cash_reg.show_all()

# Checking that all instances of bread in items list has been removed
# and that it has been removed from the dict list
# and that the total has decreased to only be the price of croissant.
print("\nExample removal")
cash_reg.remove_item('bread')
cash_reg.show_items()
cash_reg.get_total()
cash_reg.show_all()

# Checking that everything is empty/0 after resetting register.
print("\nExample reset")
cash_reg.reset_register()
cash_reg.show_items()
cash_reg.get_total()
cash_reg.show_all()

