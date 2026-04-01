import utils
a =[]

# na GUI quando tiver s/n pode colocar varios botoes que vao redirecionar para o que voce quer fazer
# tipo 4 botao, um pra ler, pra criar, deletar e atualizar, ficando tudo em uma so tela ao inves de cada um
# ficar te perguntando toda vez

es="s"
while es == "s":
    print(" ")
    print("Oque voce quer fazer?")
    print("Criar | Ler | Atualizar | Deletar")
    print(" ")

    faz=input().lower()
    if faz == "criar" or faz == "ler" or faz == "atualizar" or faz == "deletar":
        eval(f"utils.{faz}(a)")
    else:
        print("escolha e digite apenas uma das 4 opções")
    es=input("continuar?").lower()
