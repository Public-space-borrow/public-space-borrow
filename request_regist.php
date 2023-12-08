<?php
    session_start();
    if(isset($_POST['id'])) {
        include 'connect_db.php';
        // echo "SELECT * FROM Register where Space_id = ".$_POST['id']." ORDER BY Start_time;";
        $stmt = $conn->query("SELECT Start_time, Space_id, Date, user_id, user_name, user_phone, user_dormnumber FROM Register where Space_id = ".$_POST['id']." ORDER BY Start_time;");
        $data = $stmt->fetchAll(PDO::FETCH_ASSOC);
        if($_SESSION['mode'] != "admin") {
            for($i = 0; $i < count($data); $i++) {
                $ori_name = $data[$i]['user_name'];
                $encode_name = mb_substr($ori_name, 0, 1)."Ｏ".mb_substr($ori_name, 2, 1);
                $data[$i]['user_name'] = $encode_name;
                $data[$i]['user_id'] = mb_substr($data[$i]['user_id'], 0, 5)."ＯＯＯＯＯ";
                #如果非管理者，直接不要傳手機號碼
                $data[$i]['user_phone'] = "";
            }
        }
        $json = json_encode($data);
        // 使用echo函數將字串輸出給前端
        echo $json;
    }
    else {
        throw new Exception("Error");
    }
?>