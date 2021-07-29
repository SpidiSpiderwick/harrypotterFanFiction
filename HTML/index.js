$(document).ready(function(){
    $(".arrow").on("click",function() {
        alert("Clicked")
    });
    $(".button").click(function () {
        var div= $("#"+this.value);
        div.toggle("slow").siblings().hide("slow");
    });
});

$(function() {
    $('.arrow').hover(function(){
            $(this).addClass('hovered');
        },
        function(){
            $(this).removeClass('hovered');
        });
});