import datetime
Tim=datetime.datetime.now()
# lembrar do CRUD
# estrutura basica q vai ser trabalhada, so precisa achar um jeito de massificar isso ai 🌎🌎🌌

a =[]

# na GUI quando tiver s/n pode colocar varios botoes que vao redirecionar para o que voce quer fazer
# tipo 4 botao, um pra ler, pra criar, deletar e atualizar, ficando tudo em uma so tela ao inves de cada um
# ficar te perguntando toda vez

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
    l["prazo"]=input("prazo?")  #colocar um sistema de selecionar data no calendario ou so aceitar dd/mm/yy quando estiver na GUI
    a.append(l)
    print(a)

#read
for m in range(len(a)):
    print(" ")
    for v in a[m]:
        print(v,a[m][v])

#update
if input("quer mudar algo? s/n")=="s":
    x= int(input("qual id?"))           #na GUI tentar fazer tipo um sistema de seleção que abre pra baixo colocar lá id 1-n
    for m in range(len(a)):             #oque vai impedir de colocar um id invalido
            if a[m]["id"] == x:
                y=input("quer mudadar oq (colocar exatamente mesmo nome)")  #mesma coisa com o valor de chave que quer alterar, fazer de uma forma que voce nao possa
                if y!="id":                                                 #escrever livremente, pq se nao o caba vai digita "id" e fude com tudo
                    a[m][y]=input("fale meu fi")                               
                    break
                else:
                     print("safado")
                     break
            else:
                print("não encontrado")
                
print(a)

#delete
if input("deletar tarefa? s/n")=="s":
    d= int(input("qual id?"))
    for m in range(len(a)):
            if a[m]["id"] == d:
                 if input(f"certeza? fazer isso deletara tarefa {a[m]["nome"]} s/n")=="s":
                       del a[m]
                       break
                 
print(a)
