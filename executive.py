from includes.commands import *
from includes.addition import creat_dict

def commands(decision):
    help_commands = """commands:
                     show - list of contacts
                     add - add new contact
                     delete - delete contact
                     show one - show one contact
                     change - change contact
                     search - search contacts
                     creat - creating dictionary for contacts
                    """
    dic = {
        "show": show,
        "add": add, 
        "delete": delete, 
        "show one": show_one, 
        "change": change,
        "creat": creat_dict,
        "search": search,
        "help": help_commands, 
        }
    if decision == "help":
        print(dic[decision])
    else:
        dic[decision]()
    
while True:
    decision = input("Commnad(type help for help): ")
    if decision == "exit":
        break
    else:
        commands(decision)
    
    

    

