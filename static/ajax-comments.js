"use strict";

function showComment(result){
    $("#add-comment-text").html(result);
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