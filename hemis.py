class Student:
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

class Group:
    def __init__(self, title, profession):
        self.title = title
        self.profession = profession
        self.group = []

    def add_student(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        phone = input("Enter your phone: ")
        email = input("Enter your email: ")
        self.group.append(Student(name, age, phone, email))

    def view_students(self):
        count = 0
        for student in self.group:
            count += 1
            print(f'{count}. name: {student.name} age: {student.age} phone: {student.phone} email: {student.email}')

    def change_student(self):
        name = input("Enter your name: ")
        age2 = int(input("Enter your age: "))
        phone2 = input("Enter your phone: ")
        email2 = input("Enter your email: ")
        for student in self.group:
            if student.name == name:
                student.age = age2
                student.phone = phone2
                student.email = email2
                print('changed student successfully')
                return

    def delete_student(self):
        name = input("Enter your name: ")
        for student in self.group:
            if student.name == name:
                self.group.remove(student)
                print('deleted successfully')

class University:
    def __init__(self, title):
        self.title = title
        self.groups = []

    def add_groups(self):
        title = input("Enter the id of the group: ")
        profession = input("Enter your profession: ")
        p1 = Group(title, profession)
        self.groups.append(p1)

    def view_group(self):
        count = 0
        for group in self.groups:
            count += 1
            print(f' {count}. group id: {group.title} profession: {group.profession}')

    def change_group(self):
        title = input("Enter the title: ")
        new_title = input("Enter the new title: ")
        for group in self.groups:
            if group.title == title:
                group.title = new_title
                print('changed group successfully')



class Hemis:
    def __init__(self, title):
        self.title = title
        self.universities = []

    def add_university(self):
        title = input("Enter the university title: ")
        self.universities.append(University(title))

    def view_university(self):
        count = 0
        for university in self.universities:
            count += 1
            print(f' {count}. university title: {university.title}')

    def change_university(self):
        title = input("Enter the university title: ")
        new_title = input("Enter the new university title: ")
        for university in self.universities:
            if university.title == title:
                university.title = new_title
                print('changed university successfully')


def group_manager(group:Group):
    print('*** Group Manager ***')
    while True:
        code = input('1. add students \n 2. view students \n 3. change students info \n 4. delete students  \n 5. quit \n > ')
        if code == '1':
            group.add_student()
            print('Students added.')
            print('=================')
        elif code == '2':
            group.view_students()
            print('Students viewed.')
            print('=================')
        elif code == '3':
            group.change_student()
            print('Students changed.')
            print('=================')
        elif code == '4':
            group.delete_student()
            print('Students deleted.')
            print('=================')
        elif code == '5':
            print('Exiting....')
            break
        else:
            print('Invalid input.')
            break

def university_manager(university:University):
    print('*** University Manager ***')
    while True:
        code = input('1. add groups \n 2. view groups \n 3. change uni name  \n 4. quit \n >' )
        if code == '1':
            university.add_groups()
            print('Groups added.')
            print('=================')
        elif code == '2':
            university.view_group()
            print('-----------------')
        elif code == '3':
            university.change_group()
            print('Groups changed.')
            print('==================')
        elif code == '4':
            print('Exiting....')
            break
        else:
            print('Invalid input.')
            break


def hemis_manager(hemis:Hemis):
    print('*** Hemis Manager ***')
    while True:
        code = input('1. add university \n 2. view university \n 3. change university name \n 4. quit \n > ')
        if code == '1':
            hemis.add_university()
            print('University added.')
            print('=================')
        elif code == '2':
            hemis.view_university()
            print('==============')
            index = int(input("otm_id :"))
            University = hemis.universities[index - 1]
            university_manager(University)

        elif code == '3':
            hemis.change_university()
            print('University changed.')
            print('=================')
        elif code == '4':
            print('Exiting....')
            break
        else:
            print('Invalid input.')
            break


def main_manager(hemis:Hemis, university:University, group:Group):
    print('*** Main Manager ***')
    while True:
        code = input('1. group details \n 2. university details \n 3. hemis details  \n 4. quit \n > ')
        if code == '1':
            group_manager(group)
        elif code == '2':
            university_manager(university)
        elif code == '3':
            hemis_manager(hemis)
        elif code == '4':
            print('Exiting....')
            break
        else:
            print('Invalid input.')
            break

if __name__ == '__main__':
    hemis = Hemis('tatu')

    univer = University("tatu_university")
    group = Group("125-23a", "backend developer")

    main_manager(hemis, univer, group)
