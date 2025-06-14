import requests  # Import the requests library to handle HTTP requests
import json

#
# Michael David 2025
#
#

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
     # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)
    print(response)
    if response.status_code == 400:
        print("Invalid text! Please try again!")
        results = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }     
    elif response.status_code == 200:
    
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
   
        #convert to a set of emotions
        emotions = formatted_response["emotionPredictions"][0]["emotion"]   

        # find emotion with highest score
        highestEmotion = max(emotions, key = emotions.get)

        results = {
            'anger': emotions["anger"],
            'disgust': emotions["disgust"],
            'fear': emotions["fear"],
            'joy': emotions["joy"],
            'sadness': emotions["sadness"],
            'dominant_emotion': highestEmotion
        }

    return(results)
    #return {'label': label, 'score': score}