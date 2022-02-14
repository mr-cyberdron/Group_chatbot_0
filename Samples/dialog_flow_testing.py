from google.cloud import dialogflow_v2beta1 as dialogflow
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Chatbotjsontocken/alex-talk-9tyb-07c7d6934909.json"

#https://gist.github.com/grepto/83c723a946a87cead07bbf9befbdd963
#Получить ответ на фразу или вопрос
def get_dialog_response(session_id, text, language_code='ru', project_id='alex-talk-9tyb'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    dialogflow_response = session_client.detect_intent(session=session, query_input=query_input)
    response = {
        'query_text': dialogflow_response.query_result.query_text,
        'intent': dialogflow_response.query_result.intent.display_name,
        'confidence': dialogflow_response.query_result.intent_detection_confidence,
        'response_text': dialogflow_response.query_result.fulfillment_text,
    }
    print(dialogflow_response)
    return response

session_id = 1

while True:
    text = input('Введите текст  ')
    responce = get_dialog_response(session_id, text)
    print(responce['response_text'])
    print(responce)
