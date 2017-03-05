"use strict";
function showComment(result){
    var li = document.createElement("li");
    var html = "<small><b>"+result.first_name + " " + result.last_name + "</b>";
    html += "<i> " + result.added_at + "</i></small><br>" + result.comment;
    li.innerHTML = html;
    var commentList = $("#comment-list");
    commentList.prepend(li);

    $("#comments").val("")
}

function submitComment(evt){
    evt.preventDefault();

    var formInputs = {
        "comment": $("#comments").val(),
        "post_id": $("#post_id").val(),
    };

    $.post("/add-comment", formInputs, showComment);
}

$("#comment-field").on("click", submitComment);