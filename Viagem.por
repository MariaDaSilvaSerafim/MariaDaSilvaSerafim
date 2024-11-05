programa {

  inteiro km, opc
  real r, p = 4.19, r1


  funcao inicio() {


  escreva("Qual vc deseja usar? \n 1-Gasolina ou 2-Álcool\n")
  leia(opc)

  escolha(opc){

  caso 1: gasolina()pare

  caso 2: alcool()pare

  caso contrario: escreva ("\nOpção inválida!!")

 }

}
  funcao gasolina(){

   escreva("digite a quantidade de km da sua viagem\n")
   leia(km)
                   r=(km/12)*6.29

  escreva("Seu km é de: ", km, "\n", "Se você optar pela gasolina terá um custo de: \n", r)
}

   funcao alcool(){

   escreva("digite a quantidade de de km sua viagem\n")
   leia(km)
                  r1=(km/10)*4.19

   escreva("Seu km é de: ", km, "\n", "Se você optar pela ácool terá um custo de: \n", r1)

 }

}
    
  

