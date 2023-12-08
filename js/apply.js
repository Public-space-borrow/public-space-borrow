
$(document).ready(function(){
    var template = $("tbody").html();
    $("#car-type").selectmenu();
    $("tbody").empty();
    var hours = show_hours();
    let space_id = $("#hidden_id").html()
    collect_regist(space_id);
    // Use the simulated data in your code
    for (var i in hours) {
        var time = hours[i].startTime;
        $("tbody").append(template);
        var $newRow = $("tr").last();
        var $firstTd = $newRow.find("td:first-child"); // 第一個 td
        var $lastTd = $newRow.find("td:last-child");   // 最後一個 td
        $firstTd.html(time);
        $lastTd.html(time);
    }
    $("#private_mode").unbind().click(function(event) {
        event.preventDefault();
        let pwd = prompt("請輸入管理者密碼:");
        if(pwd != null) {
            $.ajax({
                url : "admin_mode.php",
                type: "post",
                data: {"pwd": pwd, "mode": "login"},
                success: function(response) {
                    alert(response);
                    location.reload();
                },
                error: function(jqXHR, textStatus, errorThrown){
                    alert("AJAX error" + errorThrown);
                    console.log('Error: ' + errorThrown);
                }
            });
        }
    });
    $("#logout").unbind().click(function(event) {
        event.preventDefault();
        $.ajax({
            url : "admin_mode.php",
            type: "post",
            data: {"pwd": "", "mode":"logout"},
            success: function(response) {
                location.reload();
            },
            error: function(jqXHR, textStatus, errorThrown){
                alert("AJAX error" + errorThrown);
                console.log('Error: ' + errorThrown);
            }
        });
    });
});
function collect_regist(space_id) {
    $.ajax({
        url : "request_regist.php",
        type : "post",
        data:{'id' : $("#hidden_id").html()},
        dataType: "json",
        success: function(response) {
            for(let i in response) {
                let index = response[i].Start_time - 8;
                let days = $("tbody tr").eq(index);
                days.find("td").each(function(){
                    if(this.children[0] != null && this.children[0].innerHTML == response[i].Date) { 
                        this.children[1].innerHTML = `
                            <span>${response[i].user_name}</span><br>
                            <span class= "span2">${response[i].user_id}</span>
                        `;
                        this.children[1].innerHTML = `
                            <span>${response[i].user_name}</span><br>
                            <span class= "span2">${response[i].user_id}</span>
                        `;
                        this.classList.add('used');
                        this.classList.remove('registButt');
                        this.children[2].innerHTML = JSON.stringify(response[i]);
                    }
                });
            }
            updateButtonAct();
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("AJAX error" + errorThrown);
            console.log('Error: ' + errorThrown);
        }
    }); //initial finish
}
function show_hours() {
    var hours = [];
    var startTime = 8;  // Starting hour
    for (var hour = startTime; hour < 24; hour++) {
        var time = `${hour}:00`;
        var rowData = {
            startTime: time,
        };
        hours.push(rowData);
    }
    return hours;
}


function updateButtonAct() {
    //self but
    $(".used a").unbind().click(function(event){
        event.preventDefault();
    });
    $('.used a').unbind().click(function(event){
        event.preventDefault();
        var time = $(this).parent();
        time = time.siblings('.timeText:first').html();
        var date = $(this).parent().children("p").html();
        let detail = JSON.parse($(this).siblings('.detail:first').html());
        var panel =jsPanel.modal.create({
            theme: 'dark',
            contentSize: '280 370',
            headerTitle: '',
            position: 'center 0 0',
            content: `
            <h4>取消預約</h4>
            <h5>週${date}  ${time}</h5>
            <div id="container1">
                <div id="container_cancel">
                    <br>
                    <p>姓名：${detail.user_name}</p>
                    <p>學號：${detail.user_id}</p>
                    <p>手機號碼：${detail.user_phone}</p>
                </div>
                <form action="" method="post" class="form-container">
                    <input type="password" id="pwd" name="pwd" placeholder="資料修改密碼（自訂）" required>
                    <input type="submit" value="確認取消" class="submit" id="comfirmBut">
                </form>
            </div>
            `,
            callback: function() {
                $("#comfirmBut").click(function(event){
                    event.preventDefault();
                    console.log(pwd);
                    $.ajax({
                        url: 'add_register.php',
                        type: 'POST',
                        data: {
                            'date' : date, 
                            'Start_time': time,
                            'change_pwd': $("#pwd").val(),
                            'space_id': $("#hidden_id").html(),
                            'mode': 'delete', 
                        },
                        success: function(response){
                            alert(response);
                            panel.close();
                            location.reload(true);
                        },
                        error: function(response){
                            let log = JSON.stringify(response);
                            console.log("reservation failed!!\n");
                            console.log(response);
                        }
                    });
                });
            },
        });

    });

    //normal but
    $(".registButt a").unbind().click(function(event){
        event.preventDefault();
    });
    //clickable but
    $(".registButt a").unbind().click(function(event){
        event.preventDefault();
        var time = $(this).parent();
        time = time.siblings('.timeText:first').html();
        var date = $(this).parent().children("p").html();
        var panel = jsPanel.modal.create({
            theme: 'dark',
            contentSize: '280 390',
            headerTitle: '',
            position: 'center 0 0',
            content: `
            <h4>預約資料</h4>
            <h5>週${date}  ${time}</h5>
            <div id="container1">
                <form action="" method="post" class="form-container">
                    <input type="text" id="name" name="name" placeholder="姓名" required>
                    <input type="text" id="stu_id" name="stu_id" placeholder="學號" required>
                    <input type="room" id="room" name="room" placeholder="房號" required>
                    <input type="text" id="phone" name="phone" placeholder="手機號碼" required>
                    <input type="password" id="pwd" name="pwd" placeholder="資料修改密碼（自訂）" required>
                    <input type="submit" value="提交申請" class="submit" id="comfirmBut">
                </form>
            </div>
            `,
            callback: function(panel) {
                $("#comfirmBut").click(function(event){
                    event.preventDefault();
                    var stu_id = $("#stu_id").val().replace(/\s+/g, '');
                    var room = $("#room").val().replace(/\s+/g, '');
                    var phone = $("#phone").val().replace(/\s+/g, '');
                    var pwd = $("#pwd").val().replace(/\s+/g, '');
                    let name = $("#name").val().replace(/\s+/g, '');
                    let Space_id = $("#hidden_id").html().replace(/\s+/g, '');
                    if(stu_id.length < 1 || room.length < 1 || phone.length < 1 || pwd.length < 1) {
                        alert("請完整填寫所有欄位");
                    }
                    else if(room.length < 5 || isNaN(room)) {
                        if(!confirm("房號格式不正確。\n正確格式範例:83255\n點選確定關閉視窗，或點取消開啟床位格式表")) {
                            window.open("https://housing-osa.nsysu.edu.tw/static/file/92/1092/img/336142563.pdf", '_blank')
                        }
                    }
                    else if(stu_id < 9) {
                        alert("學號格式不正確");
                    }
                    else {
                        $.ajax({
                            url: 'add_register.php',
                            type: 'POST',
                            data: {
                                'Space_id':Space_id,
                                'Start_time': time,
                                'user_id': stu_id,
                                'user_dormnumber': room,
                                'user_phone': phone,
                                'change_pwd': pwd,
                                'mode': 'add',
                                'date': date,
                                'name': name,
                            },
                            success: function(response){
                                alert(response);
                                panel.close();
                                location.reload(true);
                            },
                            error: function(response){
                                alert("預約失敗");
                                console.log(response);
                            }
                        });
                    }
                });
            },
        });
    });
}
