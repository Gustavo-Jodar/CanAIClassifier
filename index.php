<?php
require_once  "vendor/samayo/bulletproof/src/bulletproof.php";

$image = new Bulletproof\Image($_FILES);

if($image["pictures"]){
  $image->setLocation(__DIR__ . "/uploads");
  $image->setSize(25000, 1000000);
  $image->setMime(array('jpeg', 'jpg','png'));
  $name = $image->getName();
  $extension = $image->getMime();

  $upload = $image->upload();
  //http://localhost/CanAIClassifier/canBrand/?name=$name.$extension
  if($upload){
    echo "<center>
    <p>
    <a href='http://scg-turing.ifsc.usp.br/gj/CanAIClassifier/canBrand/?name=$name.$extension' class='p-3 mb-2 bg-success text-white'>See the result! (It might take a while)</a>
    </p>
    </center>";
  }else{
      echo $image->getError();
  }
}
?>

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
    <p class="lead">This AI uses the KNN (k-Nearst Neighbors) algorithm to classificate cans photos, it's very simple and sometimes even dump.
      So, it helps if the photo has a white background, if you try to upload a photo of another thing, that is not a can, the AI will try to classificate it as a can.
    </p>
    <p>
      Furthermore, for now the only types of brand cans that the AI knows are: Guaraná, Amstel, Tônica, Brahma, Boemia, Coca-cola Coffee, Original e Petra, please test one of these.
    </p>

    <hr class="my-4">
    <center>
        <legend>You can upload your can photo through the buttons bellow.</legend>

        <form method="POST" enctype="multipart/form-data">
        <div class='form-group'>
          <input type="hidden" name="MAX_FILE_SIZE" value="1000000"/>
          <input type="file" name="pictures" accept="image/*"/>
          <input type="submit" value="upload photo"/>
        </div>
      </form>
      
      <hr class="my-4">  
        <footer>
          <p>
            The image that you upload in this site go to our database to continue to improve the AI.
          </p>  
          <p>
            Desenvolved by Gustavo Jodar
          </p>
        </footer>
    </center>
  </div>
</body>

</html>
