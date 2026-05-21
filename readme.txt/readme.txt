O arquivo app.py é o principal do sistema, sendo responsável por iniciar o Flask, criar as rotas e conectar o frontend ao backend. Nele estão as funções que permitem abrir as páginas
do sistema, criar atividades, visualizar tarefas cadastradas, atualizar informações e deletar registros. Além disso, possui a função salvar_dados(), que grava automaticamente 
todas as alterações no arquivo dados.json, garantindo a persistência das informações.
O arquivo utils.py funciona como auxiliar da lógica do sistema. Suas funções são responsáveis por gerar IDs únicos para cada atividade, criar datas automáticas, montar a estrutura das
tarefas em formato de dicionário e adicionar essas tarefas na lista principal do sistema.
O arquivo dados.json atua como um banco de dados simples. Sua função é armazenar permanentemente as atividades, matérias, notas e prazos cadastrados, permitindo que os dados
permaneçam salvos mesmo após o fechamento do sistema.
A pasta templates/ contém todas as páginas HTML do projeto. O arquivo index.html funciona como página inicial e centraliza a navegação do sistema. O criar.html possui o formulário 
utilizado para cadastrar novas atividades. O ler.html é responsável por exibir todas as tarefas cadastradas em formato de cards. O atualizar.html permite editar informações das
atividades já existentes, enquanto o deletar.html disponibiliza a remoção das tarefas cadastradas.
A pasta static/ reúne os arquivos responsáveis pela aparência e interatividade do sistema. O styles.css controla toda a estilização da interface, incluindo layout, cores, 
animações, responsividade e design dos componentes. Já o script.js adiciona funcionalidades dinâmicas à interface, como abrir e fechar a sidebar, exibir modais e controlar 
interações visuais do sistema.