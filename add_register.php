<?php
function check_sequence($conn, $space_id, $user_id, $date, $start_time) {
    $stmt = $conn->prepare(sprintf("select Start_time from Register where user_id = '%s' and Date = '%s' and Space_id = %d ORDER BY Start_time", $user_id, $date, $space_id));
    $stmt->execute();
    $result = $stmt->fetchAll();
    $arr = array($start_time);
    foreach($result as $row) {
        array_push($arr, $row['Start_time']);
    }
    sort($arr);
    $count = 1;
    for($i = 1; $i < sizeof($arr); $i++) {
        if($arr[$i] - $arr[$i - 1] == 1) {
            $count++;
        }
        else {
            if($count > 2) {
                return 1;
            }
            $count = 1;
        }
    }
    return $count > 2;
}
if(isset($_POST['mode'])) {
    include 'connect_db.php';
    $day = [
        "一" => 1,
        "二" => 2,
        "三" => 3,
        "四" => 4,
        "五" => 5,
        "六" => 6,
        "日" => 7,
    ];
    if($_POST['mode'] == "add") {
        //check black list
        $b_state = $conn->prepare(sprintf("select * from black_list where stu_id = '%s'", $_POST['user_id']));
        $b_state->execute();
        $black_list = $b_state->fetch();
        if($black_list != NULL) {
            echo "此學號已被列入黑名單"."\n原因:".$black_list['banned_reason']."\n解除日期".$black_list['expire_time']."\n若有疑問請至宿舍服務組詢問";
            return;
        }
        //insert
        $sql = sprintf("INSERT INTO Register (Start_time, Space_id, Date, user_id, user_phone, user_dormnumber, change_pwd, user_name) VALUES(%d, %s, '%s', '%s', '%s', %d, '%s', '%s')", $_POST['Start_time'], $_POST['Space_id'], $_POST['date'], $_POST['user_id'], $_POST['user_phone'], $_POST['user_dormnumber'], $_POST['change_pwd'], $_POST['name']);
        $stmt = $conn->prepare(sprintf("select COUNT(*) as c from Register where Start_time = %d and Date = '%s' and Space_id = %d", $_POST['Start_time'], $_POST['date'], $_POST['Space_id']));
        $stmt->execute();
        $row = $stmt->fetch();

        $stmt = $conn->prepare(sprintf("select COUNT(*) as c from Register where user_id = %d and Date = '%s' and Space_id = %d", $_POST['user_id'], $_POST['date'], $_POST['Space_id']));
        $stmt->execute();
        $count_have_regist = $stmt->fetch();
        if($row['c'] > 0) {
            echo "這個時段已經被預約！";
        }
        else if($count_have_regist['c'] >= 2 && check_sequence($conn, $_POST['Space_id'], $_POST['user_id'], $_POST['date'], (int)$_POST['Start_time'])) {
            echo "此空間不可連續預約2小時以上";
        }
        else {
            try {
                $stmt = $conn->prepare($sql);
                $stmt->execute();
                echo "預約成功"."\n使用前請至服務站出示學生證以借用鑰匙";
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
            $stmt = $conn->prepare($sql);
            $stmt->execute();
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
