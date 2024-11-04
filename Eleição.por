programa {

    inteiro votoJoao = 0, votoMariaH = 0, votoRaissa = 0, votoBrancos = 0, votoNulos = 0, voto


funcao inicio() {

    menu()
    
  }

funcao menu(){

       faca{
            
            escreva("---------------------------------\n")
            escreva("E L E I Ç Ã O sistema de votação\n")
            escreva("---------------------------------\n")
            escreva("1. Votar em João | 2. Votar em Maria.H | 3. Votar em Raissa | 4. Brancos | 5. Nulos | 6. Finalizar Votação \n")
            leia(voto)
            
            computarvoto(voto)
            limpa()     

      } enquanto(voto != 6)
       
  apuracao(votoJoao, votoMariaH, votoRaissa, votoBrancos, votoNulos )
       
}

funcao computarvoto() {
        
      escolha(voto){

      caso 1: votoJoao += 1 pare
      caso 2: votoMariaH += 1 pare
      caso 3: votoRaissa += 1 pare
      caso 4: votoBrancos += 1 pare
      caso 5: votoNulos += 1 pare
      
      caso contrario: escreva("Erro")
      
  }  
    
 }  
   
   
    funcao apuracao(){
    
     limpa()
     escreva("\n----------------------------------\n")
     escreva("\nApuração de Resultados\n")
     escreva("\n----------------------------------\n\n")
     escreva("João: ", votoJoao, "\n", "Maria.H: ", votoMariaH, "\n", "Raissa: ", votoRaissa,  "\n", "Branco: ", votoBrancos, "\n", "Nulos", votoNulos, "\n")
     escreva("\n----------------------------------\n")


  }
   

}

