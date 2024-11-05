programa {
  
  //Banco de Informações
     inteiro bagc= 3, bcon= 3, bsen= 123, i
     caracter voltar
     real saldo = 10000, limite = 500, total = limite + saldo, deposito, s
  
  funcao vetor(){

    para(i=1; i<1000; i++){

       credito[i] = 0.0

    }

    para(i=1; i<1000; i++){

       debito[i] = 0.0
        
    }




  }


funcao inicio() {  

  inteiro agc, con, sen 


  faca{

     escreva("Informe o número da agêcia: ")
     leia(agc)
     escreva("\nInforme o número da conta: ")
     leia(con)
     escreva("\nInforme a senha: ")
     leia(sen)
  limpa()

  }enquanto(bagc != agc ou bcon != con ou bsen != sen)

  menu()

}




  funcao menu(){


    inteiro opcao

    escreva("\nEscolha Uma Operação Abaixo \n")
    escreva("\n1- Saldo | 2- Extrato | 3- Saque | 4- Depósito | 5- Sair\n")
    escreva("\nOpção: ")
    leia(opcao)
    limpa()

  

    escolha(opcao){

      caso 1:
      saldo()
      pare

      caso 2:
      extrato()
      pare

      caso 3:
      saque()
      pare

      caso 4:
      deposito()
      pare

      caso 5:
      voltar()
      pare

      caso contrario: escreva("Opção Inválida. Tente Novamente")
 }

  }

funcao saldo(){

faca{

escreva("Deseja voltar para o ínicio s|n?\n")
escreva("Saldo:", saldo, "\n")
escreva("Limite:", limite, "\n")
escreva("Total:", total, "\n\n")
escreva("-------------------\n\n")



    escreva("Deseja voltar ao menu principal s|n? ")
    leia(voltar)

   }
    enquanto(voltar != "s")
    limpa()
    menu()

}  
       
funcao extrato(){
  faca{

escreva(saldo + deposito, "\n\n")
escreva("-----------------\n\n")

escreva("Deseja voltar ao menu principal s|n?\n")
leia(voltar)

  }
    enquanto(voltar != "s")
    limpa()
    menu()
}  

funcao deposito(){
 faca{

   escreva("Qual valor deseja depositar: ")
   leia(deposito)
   escreva("---------------------------\n\n")

    para(inteiro i = 0; i < 1000; i++){
se(credito[i] == 0){

    credito[i] = deposito
    pare

  }
    }

   escreva("Deseja voltar ao menu principal s|n? ")
   leia(voltar)
 
 }
   enquanto(voltar != "s")
   limpa()
   menu()
}
 
 funcao saque(){

    faca{

       escreva("Qual valor você deseja sacar: ")
       leia(s)
       escreva("-------------------------\n\n")



       se(saldo < s){
          escreva("Valor indisponível")


       }

        s - saldo
          
        para(inteiro i = 0; i < 1000; i++){
se(debito[i] == 0){

    debito[i] = s
    pare

  }
    }

        escreva("Deseja voltar ao menu principal s|n?")
             leia(voltar)

    }
     enquanto(voltar != "s")
     limpa()
     menu()
  
  

  }  







  
} 










