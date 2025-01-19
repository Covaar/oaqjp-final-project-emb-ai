from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Flask application for emotion detection
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """Endpoint to analyze emotions from the provided text."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract emotion scores and the dominant emotion from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!."

    else:
        # Devuelve una cadena formateada con las emociones y la dominante
        return (
        f"Para la frase dada, la respuesta del sistema es 'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score} y 'sadness': {sadness_score}. La emoción dominante es {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """Renders the index page for the application."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
