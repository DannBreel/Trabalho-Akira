O código cria uma lista "a" vazia, cria a variável "faz", se ela for diferente de "sair", vai imprimir o menu das ações da agenda, se for digitado
"sair", vai encerrar totalmente o processo. Depois, o programa lê a entrada do usuário com input() e usa .lower() para garantir que o texto fique 
em minúsculo, evitando problemas com maiúsculas. Em seguida, há uma verificação: se o valor digitado for uma das opções válidas 
("criar", "ler", "atualizar" ou "deletar"), o código executa dinamicamente uma função do módulo utils usando 
eval(f"utils.{faz}(a)"). Isso significa que, dependendo do que o usuário digitou, será chamada a função correspondente (utils.criar(a), utils.ler(a), etc.), sempre passando a lista a como argumento.