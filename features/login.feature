Funcionalidade: Login do usuário

  Como um usuário do BugBank,
  Eu quero fazer login no sistema,
  Para que eu possa acessar minha conta e gerenciar minhas finanças online.

  Contexto: User na Página de Login
    Dado que o usuário está na página de login do BugBank

  Cenário: Login com credenciais válidas
    Quando o usuário fazer login com o email "usuario@valido.com" e senha "senha_valida"
    Então o usuário deve ser autenticado com sucesso
    E o sistema deve redirecionar o usuário para a página inicial

  Cenário: Login com usuario não cadastrado
    Quando o usuário tentar fazer login com o email "usuario@naocadastrado.com" e senha "senha_qualquer" não cadastrados
    Então o sistema deve exibir uma mensagem informando "Usuário ou senha inválido."
    E o usuário não deve ser autenticado