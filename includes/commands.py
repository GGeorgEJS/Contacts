import re
from includes.addition import get_dict
from includes.addition import refresh
def add():    
        while True:
                name = input("Name: ")
                phone = input("Phone: ")
                dic = get_dict()
                name_proverka = re.search("[0-9]", name)
                phone_proverka = re.search("[a-zA-Z]", phone)
                if not bool(name_proverka):
                        if not bool(phone_proverka):
                                if name in dic.keys():
                                        print("Already exist, try again")
                                        continue
                                else:
                                        dic[name] = phone
                                        break
                        else:
                                print("Phone number isn't correct, try again!")
                                continue
                else:
                        print("Wrong name, try again!")
                        continue
        print("Added new contact")
        refresh(dic)

def change():
    dic = get_dict()
    name = input("Which change: ")
    phone = input("New number: ")
    for key in dic:
        if key == name:
            dic[name] = phone
    print(f"Contact {name} has been changed")
    refresh(dic)

def delete():
    name = input("Delete name: ")
    dic = get_dict()
    if name in dic.keys():
        dic.pop(name)
        print(f"Contact {name} has been deleted")
    else:
        print("Wrong name")
    refresh(dic)

def search():
    res = ''
    dic = get_dict()
    name = input("Search: ")
    if name in dic:
        res += "{}{:>10}\n".format(name, dic[name])

    print(res)

def show_one():
    res = ""
    name = input("Name: ")
    dic = get_dict()
    if name in dic.keys():
        res += "{}{:>10}".format(name, dic[name])
    return print("Contact: ", res)

def show():
    res = ''
    dic = get_dict()
    for key in dic:
        res += "{:>5}{:>10}\n".format(key, dic[key])
    return print("All contacts:\n",res)