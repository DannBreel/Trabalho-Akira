import datetime
Tim=datetime.datetime.now()
# lembrar do CRUD
# estrutura basica q vai ser trabalhada, so precisa achar um jeito de massificar isso ai 🌎🌎🌌

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

#read
for m in range(len(a)):
    print(" ")
    for v in a[m]:
        print(v,a[m][v])

#update
if input("quer mudar algo? s/n")=="s":
    x= int(input("qual id?"))
    for m in range(len(a)):
            if a[m]["id"] == x:
                y=input("quer mudadar oq (colocar exatamente mesmo nome)")
                a[m][y]=input("fale meu fi")
                break
            else:
                print("não encontrado")

print(a)