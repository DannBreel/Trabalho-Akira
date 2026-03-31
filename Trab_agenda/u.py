a =[{'id': 1, 'matéria': 'geografia', 'nome': 'desenhar um mapa', 'data': '31/03/26', 'prazo': '20/05/26'},
    {'id': 2, 'matéria': 'geografia', 'nome': 'desenhar um mapa', 'data': '31/03/26', 'prazo': '20/05/26'},
    {'id': 3, 'matéria': 'geografia', 'nome': 'desenhar um mapa', 'data': '31/03/26', 'prazo': '20/05/26'},
    {'id': 4, 'matéria': 'geografia', 'nome': 'desenhar um mapa', 'data': '31/03/26', 'prazo': '20/05/26'}]
#update
if input("quer mudar algo? s/n")=="s":
    x= int(input("qual id?"))
    for m in range(len(a)):
            if a[m]["id"] == x:
                y=input("quer mudadar oq (colocar exatamente mesmo nome)") #na gui tentar fazer tipo um sistema de seleção que abre pra baixo colocar lá id 1-n
                a[m][y]=input("fale meu fi")                               #oque vai impedir de colocar um id invalido
                break
            else:
                print("não encontrado")

print(a)