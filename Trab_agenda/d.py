a =[{'id': 1, 'matéria': 'geografia', 'nome': 'desenhar um mapa', 'data': '31/03/26', 'prazo': '20/05/26'},
    {'id': 2, 'matéria': 'geografia', 'nome': 'desenhar um mapa', 'data': '31/03/26', 'prazo': '20/05/26'},
    {'id': 3, 'matéria': 'geografia', 'nome': 'desenhar um mapa', 'data': '31/03/26', 'prazo': '20/05/26'},
    {'id': 4, 'matéria': 'geografia', 'nome': 'desenhar um mapa', 'data': '31/03/26', 'prazo': '20/05/26'}]

#delete
if input("deletar tarefa? s/n")=="s":
    d= int(input("qual id?"))
    for m in range(len(a)):
            if a[m]["id"] == d:
                 if input(f"certeza? fazer isso deletara tarefa {a[m]["nome"]} s/n")=="s":
                       del a[m]
                       break
                 
print(a)