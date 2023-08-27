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
        <link href="css/apply.css" rel="stylesheet" />
        
    </head>
    <body class="d-flex flex-column">
        <main class="flex-shrink-0">
            <!-- Navigation-->
            <nav class="navbar navbar-expand-lg navbar-dark bg-516464">
                <div class="container px-7">
                    <a class="navbar-brand" href="main_page.php">中山大學宿舍公共空間借用系統</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                            <li class="nav-item"><a class="nav-link" href="https://housing-osa.nsysu.edu.tw/">宿服組網站</a></li>
                            <li class="nav-item"><a class="nav-link" href="faq.html">借用須知</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="text-center mt-5 mb-4">
                <p class="lead fw-normal text-muted mb-0">借用空間：</p>
                <select class="wide" id="dropdown">
                    <option value="1-1">雨樹L棟會議室</option>
                    <option value="1-2">雨樹廣場</option>
                    <option value="1-3">翠亨L棟自煮空間</option>
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
                                <div class="timeSlot"></div>
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
                                <div class="timeSlot"></div>
                            </td>
                        </tr>
                        <!--a row of registration-->
                    </tbody>
                </table>
            </div>
            <div class="form-popup" id="myForm">
                <form class="form-container">
                    <h5>申請人資料</h5>
                    <form action="" method="post">
                        <input type="text" id="name" name="name" placeholder="姓名" required>
                        <input type="room" id="room" name="room" placeholder="房號" required>
                        <input type="text" id="phone" name="phone" placeholder="手機號碼" required>
                        <input type="submit" value="提交申請" class="submit">
                </form>
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
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
        <script src="js/apply.js"></script>
    </body>
</html>