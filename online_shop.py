class User:
    def __init__(self, name, age, phone, password):
        self.name = name
        self.age = age
        self.phone = phone
        self.password = password
        self.users_base = []

    def add_user(self):
        pass

    def remove_user(self):
        pass

    def edit_user(self):
        pass

    def view_user(self):
        pass

    def login_user(self):
        pass

class Item:
    def __init__(self, name, price, guarantee, year ):
        self.name = name
        self.price = price
        self.guarantee = guarantee
        self.year = year
        self.items_base = []

    def add_item(self):
        pass

    def remove_item(self):
        pass

    def edit_item(self):
        pass

    def view_item(self):
        pass



class Card:
    def __init__(self, holder, card_no, password, balance ):
        self.holder = holder
        self.card_no = card_no
        self.password = password
        self.balance = balance
        self.cards_base = []

    def add_card(self):
        pass

    def remove_card(self):
        pass

    def edit_card(self):
        pass

    def view_card_info(self):
        pass

    def deposit(self):
        pass



class Order:
    def __init__(self, item_name, card_no, password, order_date, get_date ):
        self.item_name = item_name
        self.card_no = card_no
        self.password = password
        self.order_date = order_date
        self.get_date = get_date
        self.orders_base = []

    def add_order(self):
        pass

    def cancel_order(self):
        pass


def users_manager():
    pass

def admin_manager():
    pass


def shop_manager():
    pass
