programa {
  
  inteiro n1, n2, r
  caracter sair
  
  funcao inicio() {
       
        menu()
       
}

  funcao menu(){

    inteiro opcao

     escreva("-------Bem Vindo a Minha Calculadora-------\n")
     escreva("\nEscolha uma opção abaixo\n")
     escreva("\n1 - Somar | 2 - Subtrair | 3 - Multiplicar | 4 - Dividir | 5- Sair\n")
     leia(opcao)
     limpa()


    escolha(opcao){

    caso 1: soma() pare
    caso 2: subtrair() pare  
    caso 3: multiplicar() pare
    caso 4: dividir() pare
    caso 5: pare
    caso contrario: escreva("Opção Inválida. Tente Novamente")
     }

}

  funcao soma(){

       faca{
       
        escreva("Digite o primeiro número: \n")
       leia(n1)
       escreva("\nDigite o segundo número: \n")
       leia(n2)
       escreva("Seu resultado é: ", n1+n2, "\n")
      
       escreva("Deseja sair e voltar ao menu s|n?\n")
       leia(sair)

  }
    enquanto(sair != "s")
    limpa()
    menu()

}
    funcao subtrair(){

       faca{
       
        escreva("Digite o primeiro número: \n")
        leia(n1)
        escreva("\nDigite o segundo número: \n")
        leia(n2)
        escreva("Seu resultado é: ", n1-n2, "\n")
      
        escreva("Deseja sair e voltar ao menu s|n?\n")
        leia(sair)

  }
    enquanto(sair != "s")
    limpa()
    menu()

}

      funcao multiplicar(){

       faca{
       
        escreva("Digite o primeiro número: \n")
        leia(n1)
        escreva("\nDigite o segundo número: \n")
        leia(n2)
        escreva("Seu resultado é: ", n1*n2, "\n")
      
        escreva("Deseja sair e voltar ao menu s|n?\n")
        leia(sair)

  }
    enquanto(sair != "s")
    limpa()
    menu()

}

     funcao dividir(){

       faca{
       
        escreva("Digite o primeiro número: \n")
        leia(n1)
        escreva("\nDigite o segundo número: \n")
        leia(n2)
        escreva("Seu resultado é: ", n1/n2, "\n")
      
        escreva("Deseja sair e voltar ao menu s|n?\n")
        leia(sair)

  }
    enquanto(sair != "s")
    limpa()
    menu()

   
}


  }




  




