
<?php
session_start();
$enteredPwd = $_POST['pwd'];
$correctPwd = '76211194';
if ($enteredPwd === $correctPwd) {
    setcookie('admin_mode', true, time() + 3600, '/');
    echo '密碼正確，已設置為管理者模式';
} else {
    echo '密碼錯誤';
}
?>

<?php
    include 'connect_db.php';
    try {
        $conn = new PDO("mysql:host=$servername;dbname=dorm", $username, $password);
        // set the PDO error mode to exception
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      } catch(PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }
    $sql = "SELECT region from Space where ID = ".$_GET['space_id'];
    $stmt = $conn->prepare($sql);
    $stmt->execute();
    $row = $stmt->fetch();
    $region = $row['region'];
    if($region == NULL) {
        echo "None";
    }
    else{
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>宿舍公共空間借用系統</title>
        <!-- Bootstrap icons-->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="css/styles.css" rel="stylesheet" />
        <link href="css/apply.css" rel="stylesheet" />
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js"></script>
        <!-- Bootstrap core JS-->
        <!-- <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script> -->
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
        <!-- <script src="js/apply.js"></script> -->
        <script src="js/admin_apply.js"></script>
        <script src="js/change_select.js"></script>
        <script src="plugin/jspanel-4.16.1/dist/jspanel.min.js"></script>
        <link href="plugin/jspanel-4.16.1/dist/jspanel.min.css" rel="stylesheet">
        <script src="plugin/jspanel-4.16.1/dist/extensions/modal/jspanel.modal.min.js"></script>
    </head>
    <body class="d-flex flex-column">
        <main class="flex-shrink-0">
            <!-- Navigation-->
            <nav class="navbar navbar-expand-lg navbar-dark bg-516464">
                <div class="container px-5">
                    <a class="navbar-brand" href="main_page.php">中山大學宿舍公共空間借用系統</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                            <div class="dropdown">
                                <button class="btn" type="button" onclick="toggleDropdown('dropdownMenu')">
                                    公共空間
                                </button>
                                <div class="dropdown-menu" id="dropdownMenu" style="display: none;">
                                    <a class="dropdown-item" href="admin_mode.php?space_id=1">雨樹L棟會議室</a>
                                    <a class="dropdown-item" href="admin_mode.php?space_id=5">武嶺會議室</a>
                                    <a class="dropdown-item" href="admin_mode.php?space_id=9">武嶺交誼廳-投影機</a>
                                    <a class="dropdown-item" href="admin_mode.php?space_id=7">翠亨B棟討論室</a>
                                    <a class="dropdown-item" href="admin_mode.php?space_id=8">翠亨B棟休憩室</a>
                                </div>
                            </div>
                            <li class="nav-item"><a class="nav-link" href="https://housing-osa.nsysu.edu.tw/">公共空間</a></li>
                            <li class="nav-item"><a class="nav-link" href="https://housing-osa.nsysu.edu.tw/p/412-1092-18050.php?Lang=zh-tw">黑名單</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
            
            
        </main>
        <!-- Footer-->
        <footer class="bg-516464 py-4 mt-auto">
            <div class="container px-5">
                <div class="row align-items-center justify-content-between flex-column flex-sm-row">
                    <div class="col-auto"><div class="small m-0 text-white">中山大學宿服組</div></div>
                    <div class="col-auto"><div class="small m-0 text-white">總機電話：07-5252-000</div></div>
                </div>
            </div>
        </footer>
    </body>
</html>
<?php
    }
?>
