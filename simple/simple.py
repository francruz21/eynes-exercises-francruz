import random


def simple_list():
    id=[]
    age=[]
    lista=[]
    for i in range(10):
        x=random.randint(1, 10)
        while(id.count(x)):
            x=random.randint(1, 10)
        id.append(x)
        age.append(random.randint(1,100))
    for i in range(10):
        lista.append({"id":id[i],"age":age[i]})
    return(lista)


def sort_list(dicts):
    return sorted(dicts, key=lambda d: d["age"])
