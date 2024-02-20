$(document).ready(function(){
    $(function() {
        // 綁定change事件到select
        $('#dropdown').on('change', function() {
            let new_space = $(this).val(); // 獲取選中的值
            let url = "regist?space_id="+new_space;
            window.location = url; // 跳轉
        });
    });
});