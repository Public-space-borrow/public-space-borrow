<?php
if(isset($_POST['mode'])) {
    $servername = "114.35.222.181";
    $username = "dormcenter";
    $password = "59365937";
    $day = [
        "一" => 1,
        "二" => 2,
        "三" => 3,
        "四" => 4,
        "五" => 5,
        "六" => 6,
        "日" => 7,
    ];
    try {
        $conn = new PDO("mysql:host=$servername;dbname=dorm", $username, $password);
        // set the PDO error mode to exception
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      } catch(PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }
    if($_POST['mode'] == "add") {
        $sql = sprintf("INSERT INTO Register (Start_time, Space_id, Date, user_id, user_phone, user_dormnumber, change_pwd, user_name) VALUES(%d, %s, '%s', '%s', '%s', %d, '%s', '%s')", $_POST['Start_time'], $_POST['Space_id'], $_POST['date'], $_POST['user_id'], $_POST['user_phone'], $_POST['user_dormnumber'], $_POST['change_pwd'], $_POST['name']);
        $stmt = $conn->prepare(sprintf("select COUNT(*) as c from Register where Start_time = %d and Date = '%s' and Space_id = %d", $_POST['Start_time'], $_POST['date'], $_POST['Space_id']));
        $stmt->execute();
        $row = $stmt->fetch();
        if($row['c'] > 0) {
            echo "這個時段已經被預約！";
        }
        else {
            try {
                $stmt = $conn->prepare($sql);
                $stmt->execute();
                echo "預約成功";
            }
            catch(Exception $e) {
                echo $e;
            }
        }
    }
    else if($_POST['mode'] == "delete"){
        // $today = date('w');
        // $date = $_POST['date'];
        // $now = date('G');
        // $r_t = $_POST['Start_time'];
        // if($today == 0) $today = $today + 7;
        // if($today < $date || ($today == $date && $now < $r_t) ) {
        //     $sql = sprintf("DELETE FROM Register where Start_time = %d and Space_id = %d and Date = '%s';", $_POST['Start_time'], $_POST['space_id'], $_POST['date']);
        //     $stmt = $conn->prepare(sprintf("SELECT change_pwd from Register where Start_time = %d and Space_id = %d and Date = '%s'", $_POST['Start_time'], $_POST['space_id'], $_POST['date']));
        //     $stmt->execute();
        //     $row = $stmt->fetch();
        //     if($row['change_pwd'] == $_POST['change_pwd']) {
        //         $conn->query($sql);
        //         echo "刪除成功！";
        //     }
        //     else {
        //         echo "變更密碼錯誤！！";
        //     }
        // }
        // else {
        //     echo "該預約已超過時間，無法變更";
        // }
        $sql = sprintf("DELETE FROM Register where Start_time = %d and Space_id = %d and Date = '%s';", $_POST['Start_time'], $_POST['space_id'], $_POST['date']);
        $stmt = $conn->prepare(sprintf("SELECT change_pwd from Register where Start_time = %d and Space_id = %d and Date = '%s'", $_POST['Start_time'], $_POST['space_id'], $_POST['date']));
        $stmt->execute();
        $row = $stmt->fetch();
        if($row['change_pwd'] == $_POST['change_pwd']) {
            $conn->query($sql);
            echo "刪除成功！";
        }
        else {
            echo "變更密碼錯誤！！";
        }
    }
}
else {
    throw new Exception("Error");
}
?>
