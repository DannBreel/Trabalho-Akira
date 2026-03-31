import datetime
Tim=datetime.datetime.now()

a =[]

#create
while input("criar nova tarefa s/n")=="s":  
    l= {}  
    if len(a)!=0: 
        l["id"]= int(a[len(a)-1]["id"])+1
    else:
        l["id"]=0
    l["matéria"]=input("materia?")
    l["nome"]=input("nome?")    
    l["nota"]=input("nota?")    #colocar um sistema de seleção tipo ]0,100]
    l["data"]=Tim.strftime("%d/%m/%y")
    l["prazo"]=input("prazo?")  #colocar um sistema de selecionar data no calendario ou so aceitar dd/mm/yy quando estiver na gui
    a.append(l)
    print(a)
