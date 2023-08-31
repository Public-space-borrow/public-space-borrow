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

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>宿舍公共空間借用系統</title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <!-- Bootstrap icons-->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body class="d-flex flex-column">
        <main class="flex-shrink-0">
            <!-- Navigation-->
            <nav class="navbar navbar-expand-lg navbar-dark bg-516464">
                <div class="container px-5">
                    <a class="navbar-brand" href="">中山大學宿舍公共空間借用系統</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                            <li class="nav-item"><a class="nav-link" href="https://housing-osa.nsysu.edu.tw/">宿服組網站</a></li>
                            <li class="nav-item"><a class="nav-link" href="faq.html">借用須知</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
            <!-- Pricing section-->
            <section class="bg-light py-5">
                <div class="container px-5 my-5">
                    <div class="text-center mb-5">
                        <h1 class="fw-bolder">請選擇想借用的空間</h1>
                        <p class="lead fw-normal text-muted mb-0">Choose the area that you want to borrow</p>
                    </div>
                    <div class="row gx-5 justify-content-center card_row">
                        <!-- Yu Shu -->
                        <div class="col-lg-6 col-xl-4">
                            <img src="pic/Yu-Shu.jpeg" alt="雨樹服務站" style="width:100%">
                            <div class="card mb-5 mb-xl-0">
                                <div class="card-body p-5">
                                    <ul class="list-unstyled mb-4">
                                        <?php
                                            $sql = "SELECT * FROM Space where region = '雨樹'";
                                            foreach($conn->query($sql) as $row) {
                                                if($row['link'] != NULL) {
                                                    $link = $row['link'];
                                                }
                                                else {
                                                    $link = "apply.php?space_id=".(string)$row['ID'];
                                                }
                                        ?>
                                            <li class="mb-2">
                                                <a class="nav-link" href="<?=$link?>">
                                                    <i class="bi bi-pin-angle-fill"></i>
                                                    <?=$row['Space_name']?>
                                                </a>
                                            </li>
                                        <?php
                                            }
                                        ?>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <!-- Wu Ling -->
                        <div class="col-lg-6 col-xl-4">
                            <img src="pic/Wu-Ling.jpeg" alt="武嶺服務站" style="width:100%">
                            <div class="card mb-5 mb-xl-0">
                                <div class="card-body p-5">
                                    <ul class="list-unstyled mb-4">
                                        <?php
                                            $sql = "SELECT * FROM Space where region = '武嶺'";
                                            foreach($conn->query($sql) as $row) {
                                                if($row['link'] != NULL) {
                                                    $link = $row['link'];
                                                }
                                                else {
                                                    $link = "apply.php?space_id=".(string)$row['ID'];
                                                }
                                        ?>
                                            <li class="mb-2">
                                                <a class="nav-link" href="<?=$link?>">
                                                    <i class="bi bi-pin-angle-fill"></i>
                                                    <?=$row['Space_name']?>
                                                </a>
                                            </li>
                                        <?php
                                            }
                                        ?>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <!-- Cuei Heng -->
                        <div class="col-lg-6 col-xl-4">
                            <img src="pic/Cuei-Heng.jpeg" alt="翠亨服務站" style="width:100%">
                            <div class="card mb-5 mb-xl-0">
                                <div class="card-body p-5">
                                    <ul class="list-unstyled mb-4">
                                        <?php
                                            $sql = "SELECT * FROM Space where region = '翠亨'";
                                            foreach($conn->query($sql) as $row) {
                                                if($row['link'] != NULL) {
                                                    $link = $row['link'];
                                                }
                                                else {
                                                    $link = "apply.php?space_id=".(string)$row['ID'];
                                                }
                                        ?>
                                            <li class="mb-2">
                                                <a class="nav-link" href="<?=$link?>">
                                                    <i class="bi bi-pin-angle-fill"></i>
                                                    <?=$row['Space_name']?>
                                                </a>
                                            </li>
                                        <?php
                                            }
                                        ?>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
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
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
        
    </body>
</html>

