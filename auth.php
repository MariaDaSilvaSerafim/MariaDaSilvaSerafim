<?php
session_start();
// Obtendo os dados do Formulário
$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

$users = json_decode(file_get_contents('users.json'), true);

$autenticado = false;

foreach($users as $user){
    if($user['username' == $username] && $user['password' == $password]){
        $autenticado = true;
        break;
    }
}

// Redirecionando o Usuário
if($autenticado){
    header("Location: painel.php");
    exit();
}
else{
    header("Location: Index.php?Usuário ou senha inválidas");
    exit();
}
?>
