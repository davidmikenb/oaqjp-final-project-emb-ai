from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route('/')
def render_homepage():
    
    return render_template("index.html")

@app.route("/emotionDetector", methods = ["GET"])
def sent_analyzer():
    text = request.args.get('textToAnalyze')

    response = emotion_detector(text)

    if response["dominant_emotion"] is None:
        result = "Invalid text! Please try again!"
    else:
        result = "For the given statement, the system response is"

        for key, value in response.items():
            # dominant emotion is mentioned separately as its own sentence.
            if key != "dominant_emotion":
                result += f" '{key}': {value},"
        # Replace last comma with point. If index is -1, no commas found.
        last_comma_index = result.rfind(",")
        if last_comma_index != -1:
            result = result[:last_comma_index] + '.' + result[last_comma_index + 1:]
        
        result += f" The dominant emotion is {response['dominant_emotion']}."

    return result



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5010)
    #app.run(debug=True)