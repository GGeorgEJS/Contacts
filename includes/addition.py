import pickle
def creat_dict():
    dict_ = {}
    with open("dict.pickle", "wb") as dict_of_contacts:
        pickle.dump(dict_, dict_of_contacts)
        #Создаеться файл в который будет сохраняться словарь 
def get_dict():
    with open("dict.pickle", 'rb') as dict_of_contacts:
            dict_ = pickle.load(dict_of_contacts)
            return dict_
        #Достаем словарь с файла и возвращаем его
        
def refresh(dict_of_contacts):
    with open("dict.pickle", "wb") as dict_:
        pickle.dump(dict_of_contacts, dict_)
        #Получаем обновленный словарь и перезаписыаем его в файл
