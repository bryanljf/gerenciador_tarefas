# Gerenciador de Tarefas Web

## Resumo do Projeto
Projeto de uma aplicação web simulando um gerenciador de tarefas semelhante ao Trello, com
funcionalidades de criação, edição, remoção e direcionamento de tarefas para usuários do sistema.
Trabalho desenvolvido para a disciplina de "Tópicos Especiais em Software" da Universidade Positivo.

## Tecnologias
Projeto criado com:
* Python versão 3.12.4
* Django versão 5.1.1
* HTML5
* CSS

## Setup
Para rodar o projeto, execute os seguintes passos abaixo:
* No terminal ou prompt de comando, acesse a pasta do projeto
* Execute o seguinte comando para iniciar o servidor local:
```
python manage.py runsserver
```
* Acesse no navegador, o endereço mostrado no Terminal/Prompt

## Instruções/Funcionalidades
* Para iniciar, selecione a opção de registro para criar um novo usuário
  (O e-mail deve ser válido e a senha deve ter, no mínimo 8 carácteres)
* Após o registro, faça o login com o seu novo usuário
* Para criar uma nova tarefa, selecione a opção de criação de tarefas no menu principal
  (Por padrão, todas as novas tarefas são criadas com o status "Pendente")
* Nomeie a tarefa como for mais apropriado e forneça sua descrição, além do usuário responsável pela tarefa
  (Caso não seja apontado um usuário, o sistema automaticamente direciona para quem criou a tarefa)
* Para visualizar suas tarefas, selecione a opção "Minhas Tarefas" no menu principal
* Para editar ou remover uma tarefa, deve-ser selecionar a opção "Editar Tarefa" na área "Minhas Tarefas"
  (Apenas as tarefas direcionadas ao usuário podem ser editadas/removidas)
* Para visualizar todas as tarefas do grupo de usuários do sistema, selecionar a opção "Todas as tarefas" no menu principal
* Para visualizar todos os usuários do sistema, selecionar a opção de lista de usuários no menu principal
