
<?php
session_start();
$enteredPwd = $_POST['pwd'];
$correctPwd = '76211194';
if($_POST['mode'] == "login") {
    if ($enteredPwd === $correctPwd) {
        $_SESSION['mode'] = "admin";
        echo '密碼正確，已設置為管理者模式'.$_SESSION['mode'];
    } else {
        echo '密碼錯誤';
    }
}
else if($_POST['mode'] == "logout") {
    $_SESSION['mode'] = "normal";
}
?>