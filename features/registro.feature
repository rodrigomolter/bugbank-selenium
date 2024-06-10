# language: pt
Funcionalidade: Cadastro de Usuário no BugBank
  Como um novo usuário do BugBank,
  Eu quero me cadastrar no sistema,
  Para que eu possa utilizar os serviços oferecidos.

  Contexto: Usuário na tela de cadastro
    Dado que o usuário está na tela de cadastro do BugBank

  Cenário: Cadastro de um usuário válido
    Quando o usuário se cadastra preenchendo todos os campos corretamente
    | email             | nome    | senha    | comSaldo |
    | rodrigo@email.com | Rodrigo | p@ssw0rd | sim      |
    Então devo receber uma mensagem de criação de conta com sucesso com o número da conta criada