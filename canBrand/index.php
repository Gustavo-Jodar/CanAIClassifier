<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <title>Can classifier</title>
</head>
  <body>
    <div class="jumbotron">
      <h1 class="display-4">Artificial intelligence to identify can brands through photos</h1>

      <p class="lead">Remember: this AI is still on development, so it might make mistakes.</p>
        <center>
        <hr class="my-4">
          <p>
            <?php 
              $image = $_GET['name'];
              $resp = shell_exec("/home/gustavojodar/anaconda3/bin/python3.8 /var/www/html/gj/CanAIClassifier/canBrand/IdentifyCan/IdentificaQuaseSnake.py $image 2>&1");
              //$resp = shell_exec("/home/gustavo/miniconda3/bin/python3.7 /var/www/html/CanAIClassifier/canBrand/IdentifyCan/IdentificaQuaseSnake.py $image 2>&1");
              echo "<h1>The AI thinks that there is $resp</h1>";
            ?>
          </p>
          <p>
            <img src="../uploads/<?php echo $image;?>" width="350" height="300"/>
          </p>
          <hr class="my-4">
          
          <a href='http://scg-turing.ifsc.usp.br/gj/CanAIClassifier/' class='p-3 mb-2 bg-success text-white'>Try another</a>
        </center>
      <hr class="my-4">
        <center>
          <footer>
          <p>
            The image that you upload in this site go to our database to continue to improve the AI.
          </p>  
          <p>
            Developed by Gustavo Jodar
          </p>
        </footer>
      </center>
    </div>
  </body>

</html>
