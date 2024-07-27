Funcionalidade: Cadastro de Usuário no BugBank
  Como um novo usuário do BugBank,
  Eu quero me cadastrar no sistema,
  Para que eu possa utilizar os serviços oferecidos.

  Contexto: Usuário na tela de cadastro
    Dado que o usuário está na tela de cadastro do BugBank

  Cenário: Cadastro de um usuário válido
    Quando o usuário se cadastrar corretamente com os seguintes dados
    | email             | nome    | senha    | comSaldo |
    | rodrigo@email.com | Rodrigo | p@ssw0rd | sim      |
    Então o sistema deve exibir receber uma mensagem de criação de conta com sucesso com o número da conta criada

  Esquema do Cenário: Tentativa de cadastro sem preencher campo
    Quando o usuário tenta se cadastrar sem preencher o campo de <campo>
    Então o sistema deve exibir a mensagem de campo obrigatório

    Exemplos:
    | campo           |
    | nome            |
    | email           |
    | senha           |
    | confirmar senha |


  Cenário: Cadastro de usuário com senhas diferentes
    Quando o usuário preencher o formulário de cadastro com o campo de senha com "senha123"
    E preencher o campo de confirmação de senha com "outrasenha123"
    Então o alerta de "As senhas não são iguais." deve ser exibido

  Cenário: Cadastro com a opção "criar conta com saldo" marcada
    Quando o usuário preencher todos os campos obrigatórios corretamente
    E o usuário selecionar a opção "Criar conta com saldo"
    Então o sistema deve exibir receber uma mensagem de criação de conta com sucesso com o número da conta criada
    E o sistema deve criar a conta com um saldo de "R$ 1.000,00"

  Cenário: Cadastro com a opção "criar conta com saldo" desativada
    Quando o usuário preencher todos os campos obrigatórios corretamente
    E o usuário não selecionar a opção "Criar conta com saldo"
    Então o sistema deve exibir receber uma mensagem de criação de conta com sucesso com o número da conta criada
    E o sistema deve criar a conta com um saldo de "R$ 0,00"