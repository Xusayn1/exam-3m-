import csv
import os
import re

from contourpy.util import data


def validate_phone(phone):
    """
    O'zbekiston telefon raqamini tekshiradi
    Formatlar:
    - +998912345678
    - 998912345678
    - 912345678
    - 91 234 56 78
    - (91) 234-56-78
    """
    cleaned_phone = re.sub(r'[\s\(\)\-+]', '', phone)

    if not cleaned_phone.isdigit():
        return False, "Phone number should contain only digits"

    if len(cleaned_phone) == 9:
        return True, f"+998{cleaned_phone}"
    elif len(cleaned_phone) == 12 and cleaned_phone.startswith('998'):
        return True, f"+{cleaned_phone}"
    elif len(cleaned_phone) == 13 and cleaned_phone.startswith('998'):
        return True, cleaned_phone
    else:
        return False, "Invalid phone number format. Examples: 912345678, 998912345678, +998912345678"


def validate_id(id_str):
    if id_str.isalnum():
        return True, ""
    else:
        return False, "ID should contain only letters and numbers"


def add_contacts():
    name = input("Enter your name: ")

    while True:
        phone = input("Enter your phone number: ")
        is_valid, message = validate_phone(phone)
        if is_valid:
            phone = message
            break
        else:
            print(f"Error: {message}")
            print("Please try again. Examples: 912345678, 998912345678")

    while True:
        id = input("Enter your id: ")
        is_valid, message = validate_id(id)
        if is_valid:
            break
        else:
            print(f"Error: {message}")
            print("Please try again. ID should contain only letters and numbers")

    columns = ['name', 'phone', 'id']

    file_exists = os.path.isfile('contact.csv')

    with open('contact.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(columns)


        writer.writerow([name, phone, id])

    print("Contact added successfully!")


def read_contacts():
    try:
        with open('contact.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            count = 0
            contacts = []
            for i in reader:
                if count == 0:
                    print(f"{'No.':<3} {i[0]:<15} {i[1]:<15} {i[2]:<10}")
                    print("-" * 45)
                else:
                    print(f'{count:<3} {i[0]:<15} {i[1]:<15} {i[2]:<10}')
                count += 1
                contacts.append({
                    'name': i[0],
                    'phone': i[1],
                    'category': i[2]
                })
            if count == 0:
                print("No contacts found!")
            return contacts
    except FileNotFoundError:
        print("Contact file not found! Please add some contacts first.")


def delete_contacts():
    try:

        contacts = []
        with open('contact.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                contacts.append(row)

        if len(contacts) <= 1:
            print("No contacts to delete!")
            return

        read_contacts()

        kod = input('Enter id to delete: ')

        new_contacts = [contacts[0]]

        deleted = False
        for i in range(1, len(contacts)):
            if contacts[i][2] != kod:
                new_contacts.append(contacts[i])
            else:
                deleted = True

        if deleted:

            with open('contact.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(new_contacts)
            print("Contact deleted successfully!")
        else:
            print("Contact with this id not found!")

    except FileNotFoundError:
        print("Contact file not found!")


def manager_contacts():
    while True:
        print('\n=== Contact Manager ===')
        print('1. Add contacts')
        print('2. Delete contacts')
        print('3. View contacts')
        print('4. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            add_contacts()
        elif choice == '2':
            delete_contacts()
        elif choice == '3':
            read_contacts()
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice! Please try again.')


def send_message ():
    data = read_contacts()
    if data:
        choose = input("Choose contact to send: ")
        for contact in data:
            if contact['name'] == choose:
                message = (input("Enter message to send: "))
                with open('sms.csv', 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([choose, message])
                print(f"Message sent to {choose} successfully!")
                return True
        print(f"Contact '{choose}' not found.")
        return False
    else:
        print("No contacts available.")
        return False

def delete_message ():
    try:
        with open('sms.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            messages = list(reader)

        if not  messages:
            print("No messages found.")
            return False
        choose = input("Choose message to delete: ")
        original_cont = len(messages)
        filtered_messages = [i for i in messages if i[0] != choose]
        deleted_messages = original_cont - len(filtered_messages)

        if deleted_messages == 0:
            print(f"No messages found for contact {choose}.")
            return False

        with open('sms.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(filtered_messages)

        print(f"Message deleted from {choose} successfully!")
        return True
    except FileNotFoundError:
        print("No messages file found.")
        return False


def view_messages():
    try:
        with open('sms.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            messages = list(reader)
            for message in messages:
                print(message)
        return True
    except FileNotFoundError:
        print("No messages file found.")
        return False


def manager_messages():
    while True:
        print('\n=== SMS Manager ===')
        print('1. send message \n2. delete message \n3. View message \n4. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            send_message()
        elif choice == '2':
            delete_message()
        elif choice == '3':
            view_messages()
        elif choice == '4':
            break
        else:
            print('Invalid choice! Please try again.')


def manager_SMS_Contact():
    while True:
        print('1. manager_contact \n 2. manger_sms \n 3  exit')
        kod = input('Enter kod:= ')
        if kod == '1':
            manager_contacts()
        elif kod == '2':
            manager_messages()
        elif kod == '3':
            break
        else:
            print('Invalid choice! Please try again.')
if __name__ == '__main__':
    manager_SMS_Contact()
