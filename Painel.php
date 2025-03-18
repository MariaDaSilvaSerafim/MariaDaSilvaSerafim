<?php
session_start();
if(!isset($_SESSION['username'])){
    header("Location: Index.php?erro=Acesso Negado");
    exit();
}
?>

<!DOCTYPE html>
<html lang = "pt-BR">
<head>
    <meta charset = "UTF-8">
    <meta name = "viewport" content = "width=device-width, initial-scale=1.0">
    <title>Painel</title>
</head>
<body>
    <h1>Logado no Painel</h1>
</body>
</html>
