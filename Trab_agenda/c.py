import datetime
Tim=datetime.datetime.now()

a =[]

#create
while input("criar nova tarefa s/n")=="s":  
    l= {}   
    l["id"]= len(a) + 1
    l["matéria"]=input("materia?")
    l["nome"]=input("nome?")
    l["data"]=Tim.strftime("%d/%m/%y")
    l["prazo"]=input("prazo?")
    a.append(l)
    print(a)
