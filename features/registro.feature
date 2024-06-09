# language: pt
Funcionalidade: Registro de novo usuário
  Como um novo cliente do BugBank
  Eu gostaria de poder me registrar
  Para que eu possa desfrutar das Funcionalidades do banco


  Cenário: Registro de um usuário válido
    Dado que eu estou na página de registro
    Quando eu preencho o formulário de cadastro
    | email             | nome    | senha    | comSaldo |
    | rodrigo@email.com | Rodrigo | p@ssw0rd | sim      |
    Então devo receber uma confirmação de que minha conta foi criada com sucesso