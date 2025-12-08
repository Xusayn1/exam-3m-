class User:
    users_base = []
    def __init__(self, name, age, phone, password):
        self.name = name
        self.age = age
        self.phone = phone
        self.password = password
        self.is_admin = False


    @classmethod
    def add_user(cls):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        phone = input("Enter your phone: ")
        password = input("Enter your password: ")
        cls.users_base.append(User(name, age, phone, password))
        print('added successfully')

    def remove_user(self):
        name = input("Enter your name: ")
        for user in self.users_base:
            if user.name == name:
                self.users_base.remove(user)
                print('removed successfully')

    def edit_user(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        phone = input("Enter your phone: ")
        password = input("Enter your password: ")
        for user in self.users_base:
            if user.name == name:
                user.age = age
                user.phone = phone
                user.password = password
                print('updated successfully')

    @classmethod
    def view_user(cls):
        for user in cls.users_base:
            print(f'Name: {user.name} Age: {user.age} Phone: {user.phone}')

    @classmethod
    def login_user(cls):
        attempts = 0
        while attempts < 3:
            name = input("Enter your name: ")
            password = input("Enter your password: ")

            for user in cls.users_base:
                if user.name == name and user.password == password:
                    print("Login successfully!")
                    return user, True

            attempts += 1
            print(f"Login failed! Attempts left: {3 - attempts}")

        print("Too many failed attempts. Access blocked.")
        return None, False


class Item:
    def __init__(self, title, price, guarantee, year ):
        self.title = title
        self.price = price
        self.guarantee = guarantee
        self.year = year
        self.items_base = []

    def add_item(self):
        title = input("Enter the title: ")
        price = input("Enter the price: ")
        guarantee = input("Enter the guarantee: ")
        year = input("Enter the year: ")
        self.items_base.append(Item(title, price, guarantee, year))
        print('added successfully')

    def remove_item(self):
        title = input("Enter the title: ")
        for item in self.items_base:
            if item.title == title:
                self.items_base.remove(item)
                print('removed successfully')

    def edit_item(self):
        title = input("Enter the title: ")
        price = input("Enter the price: ")
        guarantee = input("Enter the guarantee: ")
        year = input("Enter the year: ")
        for item in self.items_base:
            if item.title == title:
                item.price = price
                item.guarantee = guarantee
                item.year = year
                print('updated successfully')

    def view_item(self):
        for item in self.items_base:
            print(f'title: {item.title} price: {item.price} guarantee: {item.guarantee}')



class Card:
    def __init__(self, holder, card_no, password, balance ):
        self.holder = holder
        self.card_no = card_no
        self.password = password
        self.balance = balance
        self.cards_base = []

    def add_card(self):
        holder = input("Enter your holder: ")
        card_no = input("Enter your card_no: ")
        password = input("Enter your password: ")
        balance = int(input("Enter your balance: "))
        self.cards_base.append(Card(holder, card_no, password, balance))
        print('added successfully')

    def remove_card(self):
        holder = input("Enter the holder: ")
        for card in self.cards_base:
            if card.holder == holder:
                self.cards_base.remove(card)
                print('removed successfully')


    def view_card_info(self):
        for card in self.cards_base:
            print(f'holder: {card.holder} card_no: {card.card_no}  balance: {card.balance}')

    def deposit(self):
        deposit = int(input("Enter your deposit: "))
        self.balance += deposit
        print('balance updated successfully')


class Order:
    def __init__(self):
        self.orders_base = []

    def add_order(self, items_base, cards_base, user_name):
        print("=== ORDER MENU ===")

        if not items_base:
            print("No items available.")
            return

        for item in items_base:
            print(f"- {item.title} | Price: {item.price} | Guarantee: {item.guarantee}")

        title = input("Enter item title: ")

        chosen_item = None
        for item in items_base:
            if item.title == title:
                chosen_item = item
                break

        if not chosen_item:
            print("Item not found!")
            return

        car_no = input("Enter card number : ")

        chosen_card = None
        for card in cards_base:
            if card.card_no == car_no:
                chosen_card = card
                break

        if not chosen_card:
            print("Card not found!")
            return

        if chosen_card.balance >= int(chosen_item.price):
            chosen_card.balance -= int(chosen_item.price)

            order_info = {
                "user": user_name,
                "item": chosen_item.title,
                "price": chosen_item.price,
                "card": chosen_card.card_no
            }

            self.orders_base.append(order_info)
            print("Order completed successfully!")

        else:
            print("Not enough balance! Please deposit money!")

    def cancel_order(self, cards_base):
        title = input("Enter the item title to cancel: ")
        user_name = input("Enter your user name: ")

        found = False
        for order in self.orders_base:
            if order['item'] == title and order['user'] == user_name:
                card_obj = None
                for card in cards_base:
                    if card.card_no == order['card']:
                        card_obj = card
                        break

                if card_obj:
                    card_obj.balance += int(order['price'])

                self.orders_base.remove(order)
                print("Order canceled successfully and money refunded!")
                found = True
                break

        if not found:
            print("No matching order found!")

    def view_my_orders(self, user_name):
        print("=== MY ORDERS ===")
        found = False
        for order in self.orders_base:
            if order["user"] == user_name:
                print(f"Item: {order['item']} - Price: {order['price']} - Card: {order['card']}")
                found = True
        if not found:
            print("You have no orders.")

    def view_all_orders(self):
        print("=== ALL ORDERS ===")
        if not self.orders_base:
            print("No orders found.")

        for order in self.orders_base:
            print(f"User: {order['user']} | Item: {order['item']} | Price: {order['price']} | Card: {order['card']}")



def users_manager(user_obj: User, card_obj: Card, item_obj: Item, order_obj: Order, logged_user):
    while True:
        print('*** User manager ***')
        code = input("1. add orders\n2. view orders\n3. cancel orders\n4. edit info\n5. add card\n6. card info\n7. exit\n-> ")

        if code == '1':
            order_obj.add_order(item_obj.items_base, card_obj.cards_base, logged_user.name)
        elif code == '2':
            order_obj.view_my_orders(logged_user.name)
        elif code == '3':
            order_obj.cancel_order(card_obj.cards_base)
        elif code == '4':
            user_obj.edit_user()
        elif code == '5':
            card_obj.add_card()
        elif code == '6':
            card_obj.view_card_info()
        elif code == '7':
            print("Thank you for shopping!")
            break
        else:
            print("Invalid code!")


def admin_manager(user_obj: User, order_obj: Order):
    while True:
        print('*** Admin manager ***')
        code = input('1. add users\n2. view users\n3. remove user\n4. edit users\n5. view orders\n6. cancel orders\n7. exit\n-> ')
        if code == '1':
            user_obj.add_user()
        elif code == '2':
            user_obj.view_user()
        elif code == '3':
            user_obj.remove_user()
        elif code == '4':
            user_obj.edit_user()
        elif code == '5':
            order_obj.view_all_orders()
        elif code == '6':
            order_obj.cancel_order()
        elif code == '7':
            print('Exiting admin menu...')
            break
        else:
            print("Invalid code!")


def shop_manager(user_obj: User, item_obj: Item, card_obj: Card, order_obj: Order):
    print("=== SHOP MANAGER ===")

    logged_user, status = user_obj.login_user()
    if not status:
        print("*** Error: login failed ***")
        return

    print(f" Welcome {logged_user.name}!")

    if logged_user.is_admin:
        admin_manager(user_obj, order_obj)
    else:
        users_manager(user_obj, card_obj, item_obj, order_obj, logged_user)


user = User('Admin','21','9982312','1234')
user.is_admin = True
user.users_base.append(user)
user2 = User('Ali','24','99344312','2222')
user2.users_base.append(user2)
item = Item("PC", 1200, "1 year", "2024")
item.items_base.append(item)
card = Card("Ali", "9860 0121 2222 3333", "1111", 1600)
card.cards_base.append(card)
order1 = Order()

if __name__ == '__main__':
    shop_manager(user, item, card, order1)
