from includes.commands import *
from includes.addition import creat_dict

def commands(decision):
    dic = {
        "show": show,
        "add": add, 
        "delete": delete, 
        "show one": show_one, 
        "change": change,
        "creat": creat_dict,
        "search": search,
        }
    if decision not in dic:
        print("No such option")
    else:
        dic[decision]()
    
while True:
    decision = input("Commnad(type help for help): ")
    if decision == "exit":
        break
    elif decision == 'help':
        print("""commands:
                     show - list of contacts
                     add - add new contact
                     delete - delete contact
                     show one - show one contact
                     change - change contact
                     search - search contacts
                     creat - creating dictionary for contacts
                    """)
    else:
        commands(decision)
    
    

    

