function verResultado() {
    const resposta = {
        q1 : "a", //Rússia
        q2 : "c", //Deodoro da Fonseca
        q3 : "b", //Café
        q4 : "c" //Alemanha
    };

    let pontos = 0;

    for(let q in resposta){
        const respostase = document.querySelector(`input[name = "${q}]:checked`);
        if (respostase && respostase.value === resposta[q]) {
            pontos ++;
        }
    }

    const perguntas = Object.keys(resposta).length;
    const resultado = document.getElementById("resultado");
    resultado.innerHTML = `Você Acertou ${pontos} de ${perguntas} perguntas`
}
