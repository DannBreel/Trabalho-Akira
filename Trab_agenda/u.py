a =[{'id': 1, 'matéria': 'geografia', 'nome': 'desenhar um mapa', 'data': '31/03/26', 'prazo': '20/05/26'}]

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