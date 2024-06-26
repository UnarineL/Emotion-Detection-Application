from ibm_watson import NaturalLanguageUnderstandingV1                                                                     # type: ignore
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions                                         # type: ignore
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator                                                            # type: ignore

def format_emotion_output(emotion_data):
    formatted_result = "Detected Emotions:\n"
    for emotion, score in emotion_data.items():
        formatted_result += f"{emotion.capitalize()}: {score:.2f}\n"
    return formatted_result

def detect_emotion(text):
    authenticator = IAMAuthenticator('your-api-key')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )
    natural_language_understanding.set_service_url('your-service-url')

    response = natural_language_understanding.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()

    emotion_data = response['emotion']['document']['emotion']
    return format_emotion_output(emotion_data)
