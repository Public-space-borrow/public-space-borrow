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
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
        <script src="js/apply.js"></script>
        <script src="plugin/jspanel-4.16.1/dist/jspanel.min.js"></script>
        <link href="plugin/jspanel-4.16.1/dist/jspanel.min.css" rel="stylesheet">
        <script src="plugin/jspanel-4.16.1/dist/extensions/modal/jspanel.modal.min.js"></script>
    </head>
    <body class="d-flex flex-column">
        <main class="flex-shrink-0">
            <!-- Navigation-->
            <nav class="navbar navbar-expand-lg navbar-dark bg-516464">
                <div class="container px-7">
                    <a class="navbar-brand" href="main.html">中山大學宿舍公共空間借用系統</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                            <li class="nav-item"><a class="nav-link" href="https://housing-osa.nsysu.edu.tw/">宿服組網站</a></li>
                            <li class="nav-item"><a class="nav-link" href="notice.html">借用須知</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="text-center mt-5 mb-4">
                <p class="lead fw-normal text-muted mb-0">借用空間：</p>
                <select class="wide" id="dropdown">
                    <option value="3-1" <?php if ($_GET['option'] == '3-1') echo 'selected'; ?>>翠亨哺乳室</option>
                    <option value="3-2" <?php if ($_GET['option'] == '3-2') echo 'selected'; ?>>翠亨討論室</option>
                    <option value="3-3" <?php if ($_GET['option'] == '3-3') echo 'selected'; ?>>翠亨休憩室</option>
                </select>
            </div>
            
            <div class="container px-4 py-5 bg-f9f9ff">
                <table class="table calendar">
                    <thead>
                        <tr>
                            <th scope="col"></th>
                            <th scope="col">一</th>
                            <th scope="col">二</th>
                            <th scope="col">三</th>
                            <th scope="col">四</th>
                            <th scope="col">五</th>
                            <th scope="col">六</th>
                            <th scope="col">日</th>
                            <th scope="col"></th>
                        </tr>
                    </thead>
                    <tbody>
                        <!--a row of registration-->
                        <tr>
                            <td class="timeText">
                            </td>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                            <td class="registButt position-relative">
                                <p class="date">一</p>
                                <a href="#" class="stretched-link">
                                
                                </a>
                            </td>
                            <td class="registButt position-relative">
                                <p class="date">二</p>
                                <a href="#" class="stretched-link">
                                </a>
                            </td>
                            <td class="registButt position-relative">
                                <p class="date">三</p>
                                <a href="#" class="stretched-link">
    
                                </a>
                            </td>
                            <td class="registButt position-relative">
                                <p class="date">四</p>
                                <a href="#" class="stretched-link">
    
                                </a>
                            </td>
                            <td class="registButt position-relative">
                                <p class="date">五</p>
                                <a href="#" class="stretched-link">
    
                                </a>
                            </td>
                            <td class="registButt position-relative">
                                <p class="date">六</p>
                                <a href="#" class="stretched-link">
    
                                </a>
                            </td>
                            <td class="registButt position-relative">
                                <p class="date">日</p>
                                <a href="#" class="stretched-link">
    
                                </a>
                            </td>
                            <td class="timeText">
                            </td>
                        </tr>
                        <!--a row of registration-->
                    </tbody>
                </table>
            </div>            

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
// if ($_SERVER["REQUEST_METHOD"] == "POST") {
//     $mode = $_POST["mode"];
    
//     if ($mode == "init") {
//         // 假設你已經設置好了與資料庫的連接，並有一個名為 "Space" 的資料表
//         $dbHost = "localhost";
//         $dbUser = "root";
//         $dbPass = "0000";
//         $dbName = "table";

//         // 建立與資料庫的連接
//         $conn = new mysqli($dbHost, $dbUser, $dbPass, $dbName);

//         // 檢查連接是否成功
//         if ($conn->connect_error) {
//             die("連接資料庫失敗: " . $conn->connect_error);
//         }

//         // 執行查詢
//         $sql = "SELECT * FROM Register";
//         $result = $conn->query($sql);

//         if ($result->num_rows > 0) {
//             $dataList = array();
//             while ($row = $result->fetch_assoc()) {
//                 $dataList[] = $row;
//             }
            
//             // 返回數據給前端
//             $response = array(
//                 "now" => date("Y-m-d H:i:s"),  // 當下時間
//                 "Register" => $dataList
//             );
//             echo json_encode($response);
//         } else {
//             echo "沒有找到相應的數據";
//         }

//         // 關閉資料庫連接
//         $conn->close();
//     }
// }
?>
  
