Funcionalidade: Visualização do extrato

  Como um usuário do BugBank,
  Eu quero visualizar o extrato da minha conta,
  Para que eu possa acompanhar minhas transações financeiras.

  Contexto: Usuário na tela de Extrato
    Dado que o usuário está na tela de extrato do BugBank

  Cenário: Visualização do saldo disponível
    Então o sistema deve exibir o saldo disponível na conta do usuário

  Cenário: Visualização de transação de abertura de conta
    Quando possua criado uma conta com "Criar conta com saldo"
    Então o sistema deve exibir a transação com a data da operação e o tipo de transação "Abertura de conta"

  Cenário: Visualização de transação de transferência enviada
    Quando tiver realizado uma transferência para outra conta anteriormente
    Então o sistema deve exibir a transação com a data da operação e o tipo de transação "Transferência enviada"
    E o valor da transação deve estar em vermelho, indicando uma saída de fundos

  Cenário: Visualização de transação de transferência recebida
    Quando tiver recebido uma transferência de outra conta anteriormente
    Então o sistema deve exibir a transação com a data da operação e o tipo de transação "Transferência recebida"
    E o valor da transação deve estar em verde, indicando uma entrada de fundos

  Cenário: Visualização de transação sem comentário
    Quando tiver realizado uma transação sem descrição
    Então o sistema deve exibir a transação com a data da operação e o tipo de transação "Transferência enviada"
    E possuir a descrição "-"


