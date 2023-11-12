//Create date variable
var date = new Date().toLocaleDateString()

//Load HTML DOM
$(document).ready(function(){
    $("#display_date").html(date)
})

//Define variable to store predicted emotion
let predicted_emotion;

//HTML-->JavaScript--->Flask
//Flask--->JavaScript--->HTML

//jQuery selector and click action

$(function () {
    
    $("#predict_button").click(function () {
        //AJAX call

        let data_input = {
            "text" : $("text").val()
        }

        $.ajax({
            
            type : 'POST',
            url : '/predict-emotion',
            data : JSON.stringify(data_input),
            dataType : 'json',
            contentType : 'application/json',

            
            success : function(result){
                
                // Result Received From Flask ----->JavaScript
                predicted_emotion = result.data.predicted_emotion
                emotion_url = result.data.predicted_emo_url_img
                text = result.data.text_input

                // Display Result Using JavaScript----->HTML

                

            },
        });
    });
})

