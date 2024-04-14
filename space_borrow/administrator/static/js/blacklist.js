$(document).ready(function() {
    //預設封鎖時間游近到遠
    sort_mode = 0;

    console.log(sort_mode);

    // 封鎖時間遠近排序交換
    $('#swap').on("click", function(){
        // alert('click');
        if(sort_mode === 0){
            sort_mode = 1;
        }
        else{
            sort_mode = 0;
        }

        var table = $('#bl');
        var rows = table.find('tr.action').get(); // 获取所有行
        rows.reverse(); // 倒置行的顺序
        $.each(rows, function(index, row) {
            table.append(row); // 将倒置后的行重新插入到表格中
        });

    });

    //確定今日日期，防止解鎖日期填寫比當前日期前面
    var today = new Date().toISOString().split('T')[0];
    $('#input_time').attr('min', today);
    $('#crea_date').text(today);
    //insert blackList之ajax
    $("form").on("submit", function(event){
        event.preventDefault();
        var StuId= $("input[name='input_id']").val();
        var BlackDate= $("input[name='input_time']").val();
        var Reason= $("input[name='input_reason']").val();

        if(StuId.length < 9) {
            alert("學號格式不正確");
        }
        else {
            $.ajax({
                url: 'blackList',
                type: 'POST', 
                data: {
                    'banned_reason': Reason,
                    'stu_id': StuId,
                    'expire_time': BlackDate,
                    'creation_date': today,
                    "mode": "blacklist_input",
                },
                success: function(response){
                    alert(response);
                    if(response !== "該學號已存在於黑名單內")
                        location.reload(true);
                },
                error: function(response){
                    alert("輸入失敗");
                    console.log(response);
                }
            });
        }
    });

    //edit blackList
    $(".edit").on("click", function(event){
        var $row = $(this).closest(".action");

        $row.find(".edit").css("display", "none");
        $row.find(".delete").css("display", "none");
        $row.find(".save").css("display", "inline");
        $row.find(".cancel").css("display", "inline");


        var stuId = $(this).closest("tr").find("td:first").text().trim();
        var bannedReason = $(this).closest("tr").find("td:nth-child(2)").text().trim();
        var expireTime = $(this).closest("tr").find("td:nth-child(3)").text().trim();   
        // editable
        // alert(stuId + expireTime +bannedReason);


    // 迭代所有可編輯的元素，隱藏 <span>，顯示相應的 <input>
        $row.find(".editable span").each(function() {
            $(this).css("display", "none");
        });

        $row.find(".editable input").each(function() {
            $(this).css("display", "inline");
        });

        $row.find(".edit_id").val(stuId);
        $row.find(".edit_reason").val(bannedReason);

        var formattedExpireTime = expireTime.replace(/(\d{4})(\d{2})(\d{2})/, "$1-$2-$3");
        $row.find(".edit_time").val(formattedExpireTime);
        // alert(formattedExpireTime);
    });

    //save按鈕之行為
    $(".save").on("click", function(event){
        event.preventDefault();

        var $row = $(this).closest(".action");

        var original_stuId = $row.find(".ori_id").text().trim();

        var stuId = $row.find(".edit_id").val();
        var expireTime = $row.find(".edit_time").val();
        var bannedReason = $row.find(".edit_reason").val();

        $.ajax({
            url: 'blackList',
            type: 'POST', 
            data: {
                'banned_reason': bannedReason,
                'stu_id': stuId,
                'expire_time': expireTime,
                'original_id': original_stuId,
                'mode' : 'blacklist_edit',
            },
            success: function(response){
                alert(response);
                location.reload(true);
            },
            error: function(response){
                alert("修改失敗");
                console.log(response);
            }
        });
    });
    
    //取消按鈕之動作
    $(".cancel").on("click", function(event){
        var $row = $(this).closest(".action");

        $row.find(".edit").css("display", "inline");
        $row.find(".delete").css("display", "inline");
        $row.find(".save").css("display", "none");
        $row.find(".cancel").css("display", "none");

        $row.find(".editable span").each(function() {
            $(this).css("display", "inline");
        });

        $row.find(".editable input").each(function() {
            $(this).css("display", "none");
        });
    });

    //刪除紀錄之ajax
    $(".delete").on("click", function(event){
        var stuId = $(this).closest("tr").find("td:first").text().trim();
        var expireTime = $(this).closest("tr").find("td:nth-child(2)").text().trim();
        var bannedReason = $(this).closest("tr").find("td:nth-child(3)").text().trim();
        var result = confirm("確定刪除這筆資料嗎?\n\n學號:" + stuId + "\n封鎖到期日: " + expireTime + "\n封鎖原因: " + bannedReason);

        if (result) {
            $.ajax({
                    url: 'blackList',
                    type: 'POST',
                    data: {
                        'stu_id': stuId,
                        'mode' : 'blacklist_delete',
                    },
                    success: function(response){
                        alert(response);
                        // panel.close();
                        location.reload(true);
                    },
                    error: function(response){
                        alert("delete失敗");
                        console.log(response);
                    }
            });
        }
    });
});