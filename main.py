import csv
import os
import random

AP_KEY = "dsSDR#WTGR$E32R%$GTDSFAR#$RDFFDFrtfihtgf2541545dg4edt4e48"
# FILENAME = 'contact.csv'
# FIELDnAMES = ['name', 'phone', 'email']


# def load_contacts():
#     contacts = []
#     if not os.path.exists(FILENAME):
#         return contacts
#     with open(FILENAME, 'r', newline='', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             contacts.append(row)
#     return contacts



# def save_contact(contacts):
#     with open(FILENAME, 'w', newline='', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, FIELDnAMES)
#         writer.writeheader()
#         for contact in contacts:
#             writer.writerow(contact)
#     print("Saved")



# def add_contact(contacts:list):
#     name = input('Name: ').strip().lower()
#     phone = input('Phone: ').strip().lower()
#     email = input('Email: ').strip().lower()
#     contacts.append({'name': name, 'phone': phone, 'email': email})
#     save_contact(contacts=contacts)
#     return "Contact Added"



# def search_contact(contacts):
#     query = input("Search name: ").strip().lower()
#     found = False
#     for contact in contacts:
#         if query in contact['name'].lower():
#             print(f"{contact['name']} || {contact['phone']} || {contact['email']}")
#             found = True
#     if not found:
#         print("No contact found.")   


    
# def delete_contact(contacts):
#     query = input("Name to Delete: ").strip().lower()
#     new_contacts = []
#     removed = 0
#     for contact in contacts:
#         if contact['name'].lower() == query:
#             removed += 1
#         else:
#             new_contacts.append(contact)
#     if removed > 0:
#         save_contact(new_contacts)
#         contacts = new_contacts
#         print(f"{removed} contacts deleted!")
#     else:
#         print('No contact found')
        
#     return new_contacts


# def show_all(contacts):
#     if not contacts:
#         print("Phone book is Empty")
#         return
#     print("-"* 40)
#     for contact in contacts:
#         print(f"{contact['name']} || {contact['phone']} || {contact['email']}")
#     print("-"* 40)
#     print(f"Total: {len(contacts)} contacts(s).")
    


# def main():
#     contacts = load_contacts()  
#     while True:
#         print("=== Phone Book ===")
#         print("1) Add contacts")    
#         print("2) Search contacts")    
#         print("3) Delete contacts")    
#         print("4) Show All")    
#         print("5) Exit")    
        
#         choice = input("Your choice: ").strip()
        
#         if choice == "1":
#             add_contact(contacts)
#         elif choice == "2":
#             search_contact(contacts)
#         elif choice == "3":
#             delete_contact(contacts)
#             contacts = load_contacts()
#         elif choice == '4':
#             show_all(contacts)
#         elif choice == "5":
#             print("GoodBye!")
#             break
#         else:
#             print("Invalid choice, try again")
    
  
# main() 
    
class PhoneBook:
    FILENAME = 'contact.csv'
    FIELDnAMES = ['name', 'phone', 'email']
    contacts = []
    def __init__(self):
        if not os.path.exists(PhoneBook.FILENAME):
            with open(PhoneBook.FILENAME, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, PhoneBook.FIELDnAMES)
                writer.writeheader()
                for contact in PhoneBook.contacts:
                    writer.writerow(contact)
        with open(PhoneBook.FILENAME, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                PhoneBook.contacts.append(row)
    
    def save_contact(self):
        with open(PhoneBook.FILENAME, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, PhoneBook.FIELDnAMES)
            writer.writeheader()
            for contact in PhoneBook.contacts:
                writer.writerow(contact)
        print("Saved")
        
    def add_contact(self):
        name = input('Name: ').strip().lower()
        phone = input('Phone: ').strip().lower()
        email = input('Email: ').strip().lower()
        PhoneBook.contacts.append({'name': name, 'phone': phone, 'email': email})
        self.save_contact()
        return "Contact Added"
    
    def search_contact(self):
        query = input("Search name: ").strip().lower()
        found = False
        for contact in PhoneBook.contacts:
            if query in contact['name'].lower():
                print(f"{contact['name']} || {contact['phone']} || {contact['email']}")
                found = True
        if not found:
            print("No contact found.")   
    
    def delete_contact(self):
        query = input("Name to Delete: ").strip().lower()
        new_contacts = []
        removed = 0
        for contact in PhoneBook.contacts:
            if contact['name'].lower() == query:
                removed += 1
            else:
                new_contacts.append(contact)
        if removed > 0:
            self.save_contact()
            PhoneBook.contacts = new_contacts
            print(f"{removed} contacts deleted!")
        else:
            print('No contact found')
            
        return new_contacts
    def show_all(self):
        if not PhoneBook.contacts:
            print("Phone book is Empty")
            return
        print("-"* 40)
        for contact in PhoneBook.contacts:
            print(f"{contact['name']} || {contact['phone']} || {contact['email']}")
        print("-"* 40)
        print(f"Total: {len(PhoneBook.contacts)} contacts(s).")


if __name__ == "__main__":
    app = PhoneBook()
    while True:
        print("=== Phone Book ===")
        print("1) Add contacts")    
        print("2) Search contacts")    
        print("3) Delete contacts")    
        print("4) Show All")    
        print("5) Exit")    
        
        choice = input("Your choice: ").strip()
        
        if choice == "1":
            app.add_contact()
        elif choice == "2":
            app.search_contact()
        elif choice == "3":
            app.delete_contact()
            
        elif choice == '4':
            app.show_all()
        elif choice == "5":
            print("GoodBye!")
            break
        else:
            print("Invalid choice, try again")
    



# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age  = age

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"

#     def __str__(self):
#         return self.name
#     def __int__(self):
#         return 10
#     def __float__(self):
#         pass
#     def __add__(self, other):
#         res = self.age + other.age
#         names = f"{self.name} -- {other.name}"
#         return f"{names} ============= {res}"
#     def __len__(self):
#         return len(self.name)
#     def __round__(self, ndigits=None):
#         pass

# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed

#     def bark(self):
#         return f"{self.name}: hav hav!"

#     def fetch(self, item):
#         return f"{self.name} fetched {item}!"

# class Cat(Animal):
#     def __init__(self, name, age, indoor=True):
#         super().__init__(name, age)
#         self.indoor = indoor

#     def purr(self):
#         return f"{self.name}: purrrr..."

#     def eat(self):      # Override — بازنویسی متد والد
#         return f"{self.name} eats gracefully"

# rex  = Animal("Rex", 3)
# luna = Animal("Luna", 2)

# print(type(rex))



# print(rex.sleep())        # از Animal
# print(rex.eat())          # از Animal
# print(rex.bark())         # مخصوص Dog
# print(rex.fetch("ball"))  # مخصوص Dog
# print(luna.eat())         # Override
# print(luna.purr())

# print(f"\nrex is Animal: {isinstance(rex, Animal)}")
# print(f"rex is Cat: {isinstance(rex, Cat)}")
# print(rex)
print("test")