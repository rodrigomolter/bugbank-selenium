# language: pt
Funcionalidade: Login do usuário
  Como um usuário
  Eu gostaria de poder fazer login no Bug Bank
  Para que eu possa acessar a minha conta

  Cenário: Login com sucesso
    Dado que eu esteja na página login
    Quando efetuar login com dados validos
    | email           | senha |
    | teste@email.com | s3nh@ |
    Então sou redirecionado para a Home

  Cenário: Login com usuario não cadastrado
    Dado que eu esteja na página login
    Quando efetuar login com dados invalidos
    | email           | senha |
    | email@email.com | s3nh@ |
    Então recebo aviso de email ou senha invalido