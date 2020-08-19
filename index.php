<?php
require_once  "vendor/samayo/bulletproof/src/bulletproof.php";

$image = new Bulletproof\Image($_FILES);

if($image["pictures"]){
  $image->setLocation(__DIR__ . "/uploads");
  $image->setSize(25000, 1000000);
  $image->setMime(array('jpeg', 'jpg','png'));
  $name = $image->getName();

  $upload = $image->upload();
  if($upload){
    echo"<a class='btn btn-primary btn-lg' href='http://scg-turing.ifsc.usp.br/LatinhaIA/canBrand/?name=$name' role='button'>See the result!</a>";
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
  <hr class="my-4">
  <p>You can upload your can photo through the button bellow.</p>
  <hr class="my-4">

  <form method="POST" enctype="multipart/form-data">
  <div class='form-group'>
    <input type="hidden" name="MAX_FILE_SIZE" value="1000000"/>
    <input type="file" name="pictures" accept="image/*"/>
    <input type="submit" value="upload photo"/>
  </div>
</form>  

</div>
</body>

</html>
