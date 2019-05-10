import re
from includes.addition import get_dict
from includes.addition import refresh
def add():    
#Функция создает новый контакт
    while True:
        name = input("Name: ")
        phone = input("Phone: ")
        dict_of_contacts = get_dict() 
        name_test = re.search("[0-9]", name)
        phone_test = re.search("[a-zA-Z]", phone)
        if not bool(name_test):
            if not bool(phone_test):
                if name in dict_of_contacts.keys():
                    print("Already exist, try again")
                    continue
                else:
                    dict_of_contacts[name] = phone
                    print(f"Added new contact: {name}")
                    break
            else:
                print("Phone number isn't correct, try again!")
                continue
        else:
            print("Wrong name, try again!")
            continue
    refresh(dict_of_contacts)

def change():
#Функция изменяет номер выбраного контакта
    dict_of_contacts = get_dict()
    name = input("Which change: ")
    phone = input("New number: ")
    if name in dict_of_contacts:
        dict_of_contacts[name] = phone
        print(f"Contact {name} has been changed")
    else:
        print("Contact doesn't exist")
    refresh(dict_of_contacts)

def delete():
#Функция удаляет один контакт
    name = input("Delete name: ")
    dict_of_contacts = get_dict()
    if name in dict_of_contacts:
        dict_of_contacts.pop(name)
        print(f"Contact {name} has been deleted")
    else:
        print("Wrong name")
    refresh(dict_of_contacts)

def search():
#Функция находит совпадения 
    res = ''
    dict_of_contacts = get_dict()
    name = input("Search: ")
    for key in dict_of_contacts.keys():
        if name in key:
                res += "{}{:>10}\n".format(key, dict_of_contacts[key])
    print(res)

def show_one():
#Функция выводит один контакт на экран
    res = ""
    name = input("Name: ")
    dict_of_contacts = get_dict()
    if name in dict_of_contacts.keys():
        res += "{}{:>10}".format(name, dict_of_contacts[name])
        print("Contact: ", res)
    else:
        print("Contact doesn't exist")

def show():
#Функция показывает список контактов
    res = ''
    dict_of_contacts = get_dict()
    for key in dict_of_contacts:
        res += "{:>5}{:>10}\n".format(key, dict_of_contacts[key])
    print("All contacts:\n",res)