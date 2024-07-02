$(document).ready(function(){
    $('form').submit(function(event){
        event.preventDefault();
        $.ajax({
            url: $('#ajax-url').val(),
            type: "post",
            data: $(this).serialize(),
            success: function(response){
                $("#result-text").text(response.message);
                $("#name").val("");
                $("#surname").val("");
                $("#phone").val("");
                $("#email").val("");
                $(".textarea").val("");

                if (response.status == 403){
                    $("#result-text").css('color', 'red')
                } else{
                    $("#result-text").css('color', 'green')
                };
            }
        })
    })
})