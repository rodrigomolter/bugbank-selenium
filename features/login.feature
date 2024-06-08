# language: pt
Funcionalidade: Login do usuário
  Como um usuário
  Eu gostaria de poder fazer login no Bug Bank
  Para que eu possa acessar a minha conta

  Cenário: Login com sucesso
    Dado que eu esteja na página de Login
    Quando efetuar login com dados válidos
    | email           | senha |
    | teste@email.com | s3nh@ |
    Então sou redirecionado para a Home

  Cenário: Login com email não cadastrado
  # TODO

  Cenário: Login com email inválido
  # TODO

  Cenário: Login com campos vazios
  # TODO