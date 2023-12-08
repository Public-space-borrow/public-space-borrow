<?php
    $servername = "140.117.177.166";
    $username = "dormcenter";
    $password = "59365937";
    
    try {
        $conn = new PDO("mysql:host=$servername;dbname=dorm", $username, $password);
        // set the PDO error mode to exception
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      } catch(PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }
?>