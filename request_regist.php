<?php
    if(isset($_POST['id'])) {
        $servername = "114.35.222.181";
        $username = "dormcenter";
        $password = "59365937";
        try {
            $conn = new PDO("mysql:host=$servername;dbname=dorm", $username, $password);
            // set the PDO error mode to exception
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch(PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }
        // echo "SELECT * FROM Register where Space_id = ".$_POST['id']." ORDER BY Start_time;";
        $stmt = $conn->query("SELECT * FROM Register where Space_id = ".$_POST['id']." ORDER BY Start_time;");
        $data = $stmt->fetchAll(PDO::FETCH_ASSOC);
        $json = json_encode($data);
        // 使用echo函數將字串輸出給前端
        echo $json;
    }
    else {
        throw new Exception("Error");
    }
?>