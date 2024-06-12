Funcionalidade: Transferência entre contas

  Como um usuário do BugBank,
  Eu quero transferir fundos para outra conta,
  Para que eu possa realizar transações financeiras com facilidade.

  Contexto: Usuário na tela de Transferência
    Dado que o usuário está na tela de transferência do BugBank

  Cenário: Transferência com sucesso
    E o saldo da conta do usuário é de "R$ 1.500,00"
    Quando o usuário preencher todos os campos corretamente
    E tentar realizar a transferência
    Então o sistema deve debitar o valor transferido da conta do usuário
    E a mensagem "Transferencia realizada com sucesso" deve ser exibida
    E o sistema deve redirecionar o usuário para a página de extrato

  Cenário: Transferência para conta inválida
    Quando o usuário preencher o número da conta com um valor inválido ou inexistente
    E preencher os demais campos corretamente
    E tentar realizar a transferência
    Então a mensagem "Conta inválida ou inexistente" deve ser exibida

  Cenário: Transferência com saldo insuficiente
    E o saldo da conta do usuário é de "R$ 500,00"
    Quando o usuário preencher o valor da transferência com "R$ 700,00"
    E preencher os demais campos corretamente
    E tentar realizar a transferência
    Então a mensagem "Você não tem saldo suficiente para essa transação" deve ser exibida


  Cenário: Transferência com valor igual a zero
    Quando o usuário preencher o valor da transferência com "R$ 0,00"
    E preencher os demais campos corretamente
    E tentar realizar a transferência
    Então a mensagem "Valor da transferência não pode ser 0 ou negativo" deve ser exibida
