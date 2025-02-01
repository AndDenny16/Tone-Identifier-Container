
import base64
import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify
from utils import save_to_s3, create_image
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


PORT_NUMBER = os.getenv("PORT_NUMBER")
MODEL_NAME = os.getenv("MODEL_NAME")

model = tf.keras.models.load_model(MODEL_NAME)

@app.route("/predict", methods = ["POST"])
def predict_tone():
    """
        Take in a audio file and predict the Tone
        Input: 
        event: {
            "audio" : base64 encoded audio file
            "username": user who supplied the audio 
        }
        context: {}
        Output:

    """
    if request.method == "POST":
        try:
            data = request.get_json()
            if not data: 
                return jsonify({
                    "body": "Incorrect Json"
                }), 400
            print("Process Beginning")
            #Load in Content
            audio = data.get('audio')
            username = data.get('username')
            audio_data = base64.b64decode(audio)
            #Create Spectrogram Image for Input to Model
            image, image_array = create_image(audio_data, (225, 225))
            #Save Image to S3
            save_to_s3(image, username)
            #Create Tensor from Image
            image_tensor  = np.expand_dims(image_array, axis=0)
            #Model Prediction
            prediction = model.predict(image_tensor)
            
            #POS Processing 
            index = np.argmax(prediction)
            return_value = index + 1
            print('Prediction Made', return_value)
            print(prediction[0])
            score = float(prediction[0][index])
            score = round(score, 2)
            return jsonify({
                'prediction': int(return_value),
                "score": score 
                }), 200
        
        except Exception as e:
            print("EROROR", e)
            return jsonify({
                "error": {
                    "message": "Tone Prediction Unsucessful"
                }
            }), 500
        
    else:
        return jsonify({
            'body': "Wrong Method"
        })
    

@app.route('/info', methods = ['GET']) 
def info():
    return jsonify({
        "message": "To Get a Tone from Audio Clip, use a post request to the /predict endpoint, passing in"
        " a body with username and audio"
    }), 200

@app.route('/health', methods = ['GET'])
def health():
    return jsonify({
        "message": "Server is Running"
    }), 200


if __name__ == "__main__":
    app.run('0.0.0.0', port=PORT_NUMBER, debug=False)