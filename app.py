from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *
#Import sentiment analysis


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Get Input Text from POST Request
    text_input = request.json.get("text")
   
    
    if not text_input:
        # Response to send if the input_text is undefined
        return jsonify({ "status" : "error", "message" : "Enter text to predict emotion" })
    else:  
        predicted_emotion, predicted_emotion_img_url = predict(text_input)
        
        # Response to send if the input_text is not undefined
        response = {
            "status": "success",
            "data": {
                "predicted_emotion": predicted_emotion,
                "predicted_emotion_img_url": predicted_emotion_img_url
                }  
                   }

        # Send Response         
        return jsonify(response)       

       
if __name__ == "__main__":
    app.run(debug=True)



    