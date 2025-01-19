import requests
import json

def emotion_detector(text_to_analyse):
    # Define la URL para la API de análisis de sentimientos
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Crea la carga útil con el texto a analizar
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Establece los encabezados con el ID de modelo requerido para la API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Realiza una solicitud POST a la API con la carga útil y los encabezados
    response = requests.post(url, json=myobj, headers=header)

    # Analiza la respuesta de la API
    formatted_response = json.loads(response.text)
    # Si el código de estado de la respuesta es 200, extrae el label y el score de la respuesta
    if response.status_code == 200:
        emotions_data = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions_data['anger']
        disgust_score = emotions_data['disgust']
        fear_score = emotions_data['fear']
        joy_score = emotions_data['joy']
        sadness_score = emotions_data['sadness']

        # Encuentra la emoción dominante
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotions, key=emotions.get)

    # Si el código de estado de la respuesta es 500, establece las emociones como None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # Devuelve las emociones y la dominante en un diccionario
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }