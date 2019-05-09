from includes.commands import *
from includes.addition import creat_dict

def commands(args):
    s = """commands:
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
        "help": s, 
        }
    if args == "help":
        print(dic[args])
    else:
        dic[args]()
    
while True:
    decision = input("Commnad(type help for help): ")
    if decision == "exit":
        break
    else:
        commands(decision)
    
    

    

