
$(document).ready(function(){
    var template = $("tbody").html();
    $("#car-type").selectmenu();
    $("tbody").empty();
    var hours = show_hours();
    let space_id = $("#hidden_id").html()
    collect_regist(space_id);
    // Use the simulated data in your code
    for (var i in hours) {
        var time = hours[i].Start_time;
        $("tbody").append(template);
        var $newRow = $("tr").last();
        var $firstTd = $newRow.find("td:first-child"); // 第一個 td
        var $lastTd = $newRow.find("td:last-child");   // 最後一個 td
        $firstTd.html(time);
        $lastTd.html(time);

        for (var j in hours[i]) {
            modClass(hours[i][j], $firstTd);
            modClass(hours[i][j], $lastTd);
        }
    }
    updateButtonAct();
});
function collect_regist(space_id) {
    $.ajax({
        url : "request_regist.php",
        type : "post",
        data:{'id' : $("#hidden_id").html()},
        dataType: "json",
        success: function(response) {
            console.log(response);
            for(let i in response) {
                let index = response[i].Start_time - 8;
                let days = $("tbody tr").eq(index);
                days.find("td").each(function(){
                    if(this.children[0] != null && this.children[0].innerHTML == response[i].Date) {
                        this.children[1].innerHTML = response[i].user_name + "<br>" + response[i].user_id;
                    }
                });
            }
        },
        error: function(response){
            alert("AJAX error");
            console.log(response);
        }
    }); //initial finish
}
function show_hours() {
    var hours = [];
    var startTime = 8;  // Starting hour

    for (var hour = startTime; hour < 24; hour++) {
        var time = `${hour}:00`;
        var rowData = {
            Start_time: time,
        };
        hours.push(rowData);
    }
    return hours;
}

function modClass(data, $current) {
    // if(data.status == 'US') {
    //     if(data.user_id != null) {
    //         $current.children("a").html(data.user_id);
    //         if(data.name == User.Name) {
    //             if(transTime(data.period) > Now[1] || transDate(Now[0]) != data.day) {
    //                 $current.addClass("self");
    //             }
                
    //         }
    //     }
    //     else {
    //         $current.children("a").html(data.bname_id);
    //         if(band_list.includes(data.bname_id)) {
    //             if(transTime(data.period) > Now[1] || transDate(Now[0]) != data.day) {
    //                 $current.addClass("self");
    //             }
    //         }
    //     }
    //     $current.removeClass("clickable");
    // }


    // else if(data.status == 'NA') {
    //     $current.removeClass("clickable");
    //     $current.children("a").html(data.reson);
    // }
    // else {
    //     $current.addClass("clickable");
    //     $current.removeClass("self");
    //     $current.children("a").empty();
    // }
    $current.addClass("clickable");
}


function updateButtonAct() {
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
            theme: 'primary',
            headerTitle: '申請人資料',
            headerControls: 'closeonly',
            contentSize: {width: () => window.innerWidth * 0.4, height: () => window.innerHeight * 0.3},
            animateIn: 'jsPanelFadeIn',
            position: 'center 50 50',
            closeOnBackdrop: true,
            closeOnEscape: true,
            callback: function() {
                this.content.css({ 'font-family': '微軟正黑體' });
                this.setTheme({
                    bgPanel: '#fff',
                    bgContent: '#b3b3b3',
                    colorHeader: '#1b3a59',
                    colorContent: '#black',
                    border: 'medium solid #157B75'
                });
                
                this.content.innerHTML = `
                    <form class="form-container">
                        <h5>確定預約${time} ${date}?</h5>
                        <form class="container" action="#">
                            <input type="text" id="stu_id" name="stu_id" placeholder="學號" required>
                            <input type="room" id="room" name="room" placeholder="房號" required>
                            <input type="text" id="phone" name="phone" placeholder="手機號碼" required>
                            <input type="text" id="pwd" name="pwd" placeholder="資料修改密碼（自訂）" required>
                            <button class="ui-button ui-widget ui-corner-all" id="comfirmBut">確定預約</button>
                        </form>
                    </form>`
                
                
                $("#comfirmBut").click(function(event){
                    event.preventDefault();
                    var stu_id = $("#stu_id").val();
                    var room = $("#room").val();
                    var phone = $("#phone").val();
                    var pwd = $("#pwd").val();
                    $.ajax({
                        url: '',
                        type: 'POST',
                        data: {
                            'Space_id':Space_id,
                            'Start_time': time,
                            'user_id': stu_id,
                            'user_dormnumber': room,
                            'user_phone': phone,
                            'change_pwd': pwd
                        },
                        success: function(response){
                            alert(response.result);
                        },
                        error: function(response){
                            alert("預約失敗");
                        }
                    });
                    panel.close();
                });
            },
        });
    });

    // //self but
    // $('.clickable a').unbind().click(function(event){
    //     event.preventDefault();
    //     var time = $(this).parent();
    //     time = time.siblings('.timeText:first').html();
    //     var date = $(this).parent().children("p").html();

    //     var panel =jsPanel.modal.create({
    //         theme: 'primary',
    //         headerTitle: '取消預約',
    //         headerControls: 'closeonly',
    //         contentSize: {width: () => window.innerWidth * 0.4, height: () => window.innerHeight * 0.3},
    //         animateIn: 'jsPanelFadeIn',
    //         position: 'center 50 50',
    //         closeOnEscape: true,
    //         callback: function() {
    //             this.content.css({ 'font-family': '微軟正黑體' });
    //             this.setTheme({
    //                 bgPanel: '#fff',
    //                 bgContent: '#b3b3b3',
    //                 colorHeader: '#1b3a59',
    //                 colorContent: '#black',
    //                 border: 'medium solid #157B75'
    //             });

    //             this.content.innerHTML = 
    //             '<p class="panelText">確定取消'+ time + date +'？</p>' + 
    //             '<input type="text" id="pwd" name="pwd" placeholder="輸入自訂密碼" required></input>'
    //             '<button class="ui-button ui-widget ui-corner-all" id="comfirmBut">comfirm</button>';
                

    //             $("#comfirmBut").click(function(event){
    //                 $.ajax({
    //                     url: '',
    //                     type: 'POST',
    //                     data: {
    //                         'date' : date, 
    //                         'time': time,
    //                         'change_pwd': pwd,
    //                         'mode': 'delete', 
    //                         'out': out
    //                     },
    //                     success: function(response){
    //                         if(response.result == true) {
    //                             alert("取消成功");
    //                         }
    //                         else {
    //                             alert(response.result);
    //                         }
                            
    //                     },
    //                     error: function(response){
    //                         alert("reservation failed!!");

    //                     }
    //                 });
    //                 panel.close();
    //             });
    //         },
    //     });
    // });
}
