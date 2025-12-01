class User:
    def __init__(self, name, phone, seria, age, password):
        self.name = name
        self.phone = phone
        self.seria = seria
        self.age = age
        self.password = password
        self.is_active = True
        self.is_admin = False
        self.users = []

    def add_users(self):
        name = input("What is your name? ")
        phone = input("What is your phone number? ")
        seria = input("What is your seria? ")
        age = input("What is your age? ")
        password = input("What is your password? ")
        user = User(name, phone, seria, age, password)
        self.users.append(user)
        print('User added successfully')

    def remove_users(self):
        name = input("What is your name? ")
        for user in self.users:
            if user.name == name:
                self.users.remove(user)
                print('User deleted successfully')
                return
        print("User not found.")

    def edit_users(self):
        name = input("What is your name? ")
        phone = input("What is your phone number? ")
        seria = input("What is your seria? ")
        age = input("What is your age? ")
        password = input("What is your password? ")
        for user in self.users:
            if user.name == name:
                user.phone = phone
                user.seria = seria
                user.age = age
                user.password = password
                print("User updated successfully")
                return
        print("User not found.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.name == username and user.password == password:
                return user, True
        return None, False

    def view_users(self):
        if not self.users:
            print("No users available.")
            return
        for count, user in enumerate(self.users, 1):
            print(f'{count}. Name: {user.name}, Age: {user.age}, Phone: {user.phone}, Seria: {user.seria}')


class Car:
    def __init__(self, model, brand, year, seria):
        self.model = model
        self.brand = brand
        self.year = year
        self.seria = seria
        self.is_active = True


class Order:
    def __init__(self, user_id=None, car=None, date_start=None, date_end=None):
        self.user_id = user_id
        self.car = car
        self.car_id = car.seria if car else None
        self.date_start = date_start
        self.date_end = date_end
        self.is_active = True
        self.cars = []
        self.orders = []

    def add_cars(self):
        model = input("What is your model? ")
        brand = input("What is your brand? ")
        year = input("What is your year? ")
        seria = input("What is your seria? ")
        car = Car(model, brand, year, seria)
        self.cars.append(car)
        print('Car added successfully')

    def remove_cars(self):
        seria = input("Enter car seria to remove: ")
        for car in self.cars:
            if car.seria == seria:
                self.cars.remove(car)
                print('Car deleted successfully')
                return
        print("Car not found.")

    def view_cars(self):
        if not self.cars:
            print("No cars available.")
            return
        for count, car in enumerate(self.cars, 1):
            status = "Free" if car.is_active else "Booked"
            print(f'{count}. Model: {car.model}, Brand: {car.brand}, Year: {car.year}, Seria: {car.seria}, Status: {status}')

    def view_free_cars(self):
        free_cars = [car for car in self.cars if car.is_active]
        if not free_cars:
            print("No free cars available.")
            return
        for count, car in enumerate(free_cars, 1):
            print(f'{count}. Model: {car.model}, Brand: {car.brand}, Year: {car.year}, Seria: {car.seria}')

    def add_orders(self):
        if not self.cars:
            print("No cars available to order.")
            return
        user_id = input("What is your user id? ")
        self.view_free_cars()
        car_id = input("Enter car seria to book: ")
        date_start = input("What is your date start? ")
        date_end = input("What is your date end? ")

        selected_car = None
        for car in self.cars:
            if car.seria == car_id and car.is_active:
                selected_car = car
                break

        if not selected_car:
            print("Car not found or already booked!")
            return

        order = Order(user_id, selected_car, date_start, date_end)
        self.orders.append(order)
        selected_car.is_active = False
        print("Order added successfully!")

    def remove_orders(self):
        if not self.orders:
            print("No orders to remove.")
            return
        user_id = input("What is your user id? ")
        car_id = input("What is your car id? ")
        for order in self.orders:
            if order.user_id == user_id and order.car_id == car_id:
                if order.car:
                    order.car.is_active = True
                self.orders.remove(order)
                print('Order deleted successfully')
                return
        print("Order not found.")

    def view_orders(self):
        if not self.orders:
            print("No orders available.")
            return
        for count, order in enumerate(self.orders, 1):
            car_info = f"{order.car.model} ({order.car.seria})" if order.car else order.car_id
            print(f'{count}. User ID: {order.user_id}, Car: {car_info}, Date: {order.date_start} to {order.date_end}')


def view_items(user:User, order:Order):
    while True:
        code = input("1. View Users\n2. View Cars\n3. View Orders\n4. View free cars \n 5. Return\n-> ")
        if code == '1':
            user.view_users()
        elif code == '2':
            order.view_cars()
        elif code == '3':
            order.view_orders()
        elif code == '4':
            order.view_free_cars()
        elif code == '5':
            break
        else:
            print("Invalid input!")


def add_items(user:User, order:Order):
    while True:
        code = input("1. Add Users\n2. Add Cars\n3. Add Orders\n4. Return\n-> ")
        if code == '1':
            user.add_users()
        elif code == '2':
            order.add_cars()
        elif code == '3':
            order.add_orders()
        elif code == '4':
            break
        else:
            print("Invalid input!")


def remove_items(user:User, order:Order):
    while True:
        code = input("1. Remove Users\n2. Remove Cars\n3. Remove Orders\n4. Return\n-> ")
        if code == '1':
            user.remove_users()
        elif code == '2':
            order.remove_cars()
        elif code == '3':
            order.remove_orders()
        elif code == '4':
            break
        else:
            print("Invalid input!")


def taxi_manager():
    print("*** Taxi Manager ***")
    while True:
        code = input("1. Edit Info\n2. View Free Cars\n3. Exit\n-> ")
        if code == '1':
            admin.edit_users()
        elif code == '2':
            admin.view_users()
        elif code == '3':
            break
        else:
            print("Invalid input!")


def admin_manager(admin_user:User, order:Order):
    while True:
        code = input("1. Add Panel\n2. View Panel\n3. Remove Panel\n4. Exit\n-> ")
        if code == '1':
            add_items(admin_user, order)
        elif code == '2':
            view_items(admin_user, order)
        elif code == '3':
            remove_items(admin_user, order)
        elif code == '4':
            break
        else:
            print("Invalid input!")


def taxi_park_manager(user:User, order:Order):
    print("*** Taxi Park Manager ***")
    logged_user, status = user.login()
    if status:
        if logged_user.is_admin:
            admin_manager(user, order)
        else:
            taxi_manager()
    else:
        print("*** Error: login failed ***")



admin = User('Admin','991234567','123456','30','1212')
admin.is_admin = True
admin.users.append(admin)

order = Order(None, None, None, None)

if __name__ == '__main__':
    taxi_park_manager(admin, order)
