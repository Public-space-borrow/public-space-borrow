$('#region').on('change', function() {
    $("#space").empty();
    $("#space").append("<option disabled selected value> -------- </option>");
    for(let i = 0; i < all_space.length; ++i) {
        if(all_space[i]['region'] === this.value) {
            $("#space").append(`<option value=${all_space[i]["id"]}>${all_space[i]["space_name"]}</option>`)
        }
    }
});
$("#space").on('change', function() {
    $("#reserveDate").removeAttr("disabled");
});
var time_availables = [];
$("#reserveDate").on('change', function() {
    $.ajax({
        url : "",
        type : "post",
        data:{
            'space_id' : $("#space").val(),
            'date': $("#reserveDate").val(),
            'time_search': 1,
        },
        dataType: "json",
        success: function(response) {
            time_availables = [];
            time_not = response;
            for(let i = 8; i <= 23; ++i) {
                if(response.indexOf(i) === -1) {
                    time_availables.push(i);
                }
            }
            $("#startTime").empty();
            $("#startTime").append("<option disabled selected value> -------- </option>");
            for(let i = 0; i < time_availables.length; ++i) {
                $("#startTime").append(`<option value=${time_availables[i]}>${time_availables[i]}:00</option>`);
            }
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("AJAX error" + errorThrown);
            console.log('Error: ' + errorThrown);
        }
    });
});

$("#startTime").on("change", function() {
    let now = parseInt($(this).val());
    let start_idx = time_availables.indexOf(now);
    $("#hours").empty();
    $("#hours").append("<option disabled selected value> -------- </option>");
    $("#hours").append(`<option value=${$(this).val()}>${$(this).val()}:00</option>`);
    for(let j = start_idx; time_availables[j] <= 23; ++j) {
        if(time_availables[j + 1] - time_availables[j] === 1) {
            $("#hours").append(`<option value=${time_availables[j + 1]}>${time_availables[j + 1]}:00</option>`);
        }
        else {
            break;
        }
    }
});

$("#delete").unbind().click(function() {
    let space = $(this).parent().siblings()[1].children[1].innerHTML; //要送space id 而非space name
    let date = $(this).parent().siblings()[2].children[0].innerHTML;
    let s_time = $(this).parent().siblings()[3].children[0].innerHTML;
    let e_time = $(this).parent().siblings()[4].children[0].innerHTML;
    let reason = $(this).parent().siblings()[5].children[0].innerHTML;
    let formData = {
        "delete": true,
        "space" : parseInt(space),
        "date" : date,
        "startTime" : parseInt(s_time),
        "endTime": parseInt(e_time),
        "reason": reason,
    }
    $.ajax({
        url : "",
        type : "post",
        data: formData,
        success: function(response) {
            alert("delete sucess");
            location.reload();
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("AJAX error" + errorThrown);
            console.log('Error: ' + errorThrown);
            location.reload();
        }
    });
});