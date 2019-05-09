import pickle
def creat_dict():
    dict_ = {}
    with open("dict.pickle", "wb") as dic:
        pickle.dump(dict_, dic)

def get_dict():
    with open("dict.pickle", 'rb') as dic:
            dict_ = pickle.load(dic)
            return dict_

def refresh(dic):
    with open("dict.pickle", "wb") as dict_:
        pickle.dump(dic, dict_)
