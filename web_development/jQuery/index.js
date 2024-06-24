/* $(document).ready(function() {
    $("h1").css("color", "blue");
    $("button").css("color", "red"); 
    $("button").css("background-color", "lightgreen");
}); */

/* $("h1").css("color", "blue");
$("h1").css("font-size", "7rem");
$("button").css("color", "red"); 
$("button").css("background-color", "lightgreen"); */

$("h1").addClass("big-title margin-50");
$("h2").addClass("title-h2 margin-50");
$("img").addClass("margin-50");
$("button").addClass("margin-20");
// $("button");
// $("button").text("Don't Click me");
$("button").html("<em>Hey</em>");
console.log($("img").attr("src"));
$("a").attr("href", "https://www.wired.com");

$("h1").click(function() {
    $("h1").css("color", "purple");
});
