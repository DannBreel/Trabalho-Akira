import datetime
Tim=datetime.datetime.now()
# lembrar do CRUD
# estrutura basica q vai ser trabalhada, so precisa achar um jeito de massificar isso ai 🌎🌎🌌

a =[]
l= {}

while input("criar nova tarefa s/n")=="s":     
    l["id"]= len(a) + 1
    l["mat"]=input("materia?")
    l["nom"]=input("nome?")
    l["dat"]=Tim.strftime("%d/%m/%y")
    l["prazo"]=input("prazo?")
    a.append(l)
    print(a)

