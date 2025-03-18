<?php
session_start();
if(isset($_SESSION['username'])){
    header("Location: painel.php");
}
?>

<head>
    <!DOCTYPE html>
    <html lang = "pt-BR">
    <head>
        <meta charset = "UTF-8">
        <meta name = "viewport" content="width=device-width, initial-scale=1.0">
        <title>LOGIN</title>
        <link href = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <link rel = "stylesheet" href = "styles.css">

    </head>

    <body>

        <div class = "container">
            <div class = "Logo">
                <img src = "logo.png" alt = "logo">
            </div>
            <?php
                if(isset($_GET['erro'])){
                    echo "<p class = 'erro'" . htmlspecialchars($_GET['erro']) . "</p>";
                }
            ?>
        <form action = "auth.php" method="POST"></form>
        <!-- Primeiro campo Input -->
                <div class = "input-group mb-3">
                    <span class = "input-group-text">
                        <i class = "bi bi-person"></i>
                    </span>
                        <input type = "text" class = "form-control" name = "username" placeholder = "Usuário" required>
                </div>
        <!-- Segundo campo Input -->
                 <div class = "input-group mb-3">
                    <span class = "input-group-text">
                        <i class = "bi bi-lock" ></i>
                    </span>
                        <input type = "password" class = "form-control" name = "password" placeholder = "Password" required>
                 </div>
                <!-- Botão -->
                    <button type = "submit" class = "btn btn-dark">Enter</button>

                <!-- Opções Extras -->
                <div class = "d-flex justify-content-between">
                    <div class = "form-check">
                        <input type = "checkbox" class = "form-check-input">
                        <label for = "Lembrar" class = "form-check-label">Lembrar-me</label>
                    </div>
                    <a href = "">Esqueceu sua Senha?</a>
                </div>
        </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>    </body>
    
            </form>
    </body>
</html>
