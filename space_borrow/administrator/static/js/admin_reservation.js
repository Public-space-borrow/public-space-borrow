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
    let start_idx = time_availables.indexOf($(this).val());
    $("#hours").empty();
    $("#hours").push("<option disabled selected value> -------- </option>");
    $("#hours").push("<option value=1>1</option>");
    for(let j = 0; j < 15; ++j) {
        if(time_availables[j + 1] - time_availables[j] === 1) {
            $("#hours").push(`<option value=1>1</option>`);
        }
    }
});