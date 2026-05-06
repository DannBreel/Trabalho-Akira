*Def criar(a):* Primeiro foi criada a função chamada "criar" com o parâmetro "a", que dentro dela, foi importado a biblioteca datetime, que serve para trabalhar com data e horários.
Logo em seguida, foi feito uma condição, se a agenda estiver vazia, o id vai ser zero, e se não estiver vazia, vai pegar o maior id e adicionar 1.
Depois é perguntado a matéria que deseja criar na agenda, juntamente com o nome da atividade, por ex.: prova, trabalho, a nota da atividade que você quer cadastrar na 
agenda e o prazo que é a sua atividade.

*Def ler(a)*: Se não identificar nenhum caractere na lista "a", imprime "agenda vazia", e encerra com a função "return". Ele percorre a lista a usando índices (m = 0, 1, 2...), 
cada a[m] representa um elemento da lista. O código percorre a lista a usando for m in range(len(a)), onde m é o índice de cada elemento. Para cada item, imprime uma linha em 
branco para separar os dados. Depois, for v in a[m] percorre as chaves do dicionário armazenado em a[m]. A cada repetição, print(v, a[m][v]) mostra a chave (v) e seu respectivo valor.

*Def atualizar(a)*: A função atualizar(a) permite alterar um dado dentro de uma lista de dicionários (como uma lista de tarefas). Primeiro, pede ao usuário o id da tarefa que 
deseja alterar, o valor digitado é convertido para inteiro, com "int(input...)". Caso o usuário digite algo fora do código exigido, ocorre um erro, "ValueError", e a função
é encerrada com "return". Em seguida, o código percorre a lista a usando for m in range(len(a)). Para cada elemento, verifica se o valor da chave "id" (a[m]["id"]) é igual ao 
id informado. Se encontrar o item correto, o programa pergunta qual campo deseja alterar (y). Esse valor deve ser exatamente o nome da chave existente no dicionário. 
Depois, solicita o novo valor e faz a atualização com a[m][y] = input(...). Após isso, a função é encerrada. Caso o id não corresponda ao elemento atual, 
imprime "não encontrado" e continua a busca.

*Def deletar(a)*: Serve para deletar a tarefa desejada. Se for digitado o número errado, da erro "ValueError" e a função é encerrada com "return".
Depois, o código percorre a lista a com for m in range(len(a)), acessando cada elemento por índice. Para cada item, verifica se o valor da chave "id" (a[m]["id"]) é igual ao id informado.
Quando encontra a tarefa correspondente, o programa pede uma confirmação ao usuário. A mensagem inclui o nome da tarefa (a[m]["nome"]), perguntando se realmente deseja deletar. 
Se o usuário digitar "s", o comando del a[m] remove esse elemento da lista.