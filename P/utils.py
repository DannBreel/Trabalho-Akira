import datetime
def criar_web(a, materia, nome, nota, prazo):

    Tim = datetime.datetime.now()

    l = {}

    if len(a) != 0:
        l["id"] = int(a[-1]["id"]) + 1
    else:
        l["id"] = 0

    l["matéria"] = materia
    l["nome"] = nome
    l["nota"] = nota
    l["data"] = Tim.strftime("%d/%m/%y")
    l["prazo"] = prazo

    a.append(l)
    print(a)

def ler(a):
    #read
    if len(a)==0:
         print("agenda vazia")
         return
    for m in range(len(a)):
        print(" ")
        for v in a[m]:
            print(v,a[m][v])

def atualizar(a):
    #update    
    try:
        x= int(input("qual id da tarefa a ser alterada? "))
    except ValueError:
         return
    for m in range(len(a)):
            if a[m]["id"] == x:
                y=input("quer mudadar oq (colocar exatamente mesmo nome)") #na gui tentar fazer tipo um sistema de seleção que abre pra baixo colocar lá id 1-n
                a[m][y]=input("fale meu fi")                               #oque vai impedir de colocar um id invalido
                return
            else:
                print("não encontrado")

def deletar(a):
    #delete    
    try:
        d= int(input("qual id da tarefa a ser deletada? "))
    except ValueError:
         return
    for m in range(len(a)):
            if a[m]["id"] == d:
                if input(f"certeza? fazer isso deletara tarefa {a[m]['nome']} s/n")=="s":
                    del a[m]

