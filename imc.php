<!-- <?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $nome = ($_POST['nome']);
    $peso = floatval($_POST['peso']);
    $altura = floatval($_POST['altura']);

// Calcula o IMC
$imc = $peso / ($altura * $altura);

// Classifica o IMC
if ($imc < 18.5) {
    $classificacao = "ABAIXO DO PESO!";
} elseif ($imc >= 18.5 && $imc < 25.9) {
    $classificacao = "PESO NORMAL!";
} elseif ($imc >= 25 && $imc < 30) {
    $classificacao = "SOBREPESO!";
} elseif ($imc >= 30 && $imc < 35.9) {
    $classificacao = "OBESIDADE GRAU I!";
} elseif ($imc >= 35 && $imc < 40) {
    $classificacao = "OBESIDADE GRAU II!";
} else {
    $classificacao = "OBESIDADE GRAU III (Mórbida)!";
}

// Exibe o resultado
echo "Seu IMC é: " . number_format($imc, 2) . "<br>";
echo "Classificação: " . $classificacao;
}
?> -->
