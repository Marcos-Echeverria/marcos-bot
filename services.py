import requests
import sett
import json


def obtener_Mensaje_whatsapp(message):
    if 'type' not in message:
        text = 'Mensaje no reconocido'
    typeMessage = message['type']

    if typeMessage == 'text':
        text = message['text']['body']

    return text

def enviar_Mensaje_whatsapp(data):
    try:
        whatsapp_token = sett.whatsapp_token
        whatsapp_url = sett.whatsapp_url
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + whatsapp_token}
        print("se envia ", data)
        response = requests.post(whatsapp_url,
                                 headers=headers,
                                 data=data)

        if response.status_code == 200:
            print('Mensaje enviado correctamente')
            print(response.text)
        else:
            print('Error al enviar mensaje')
            print(response.text)

        return 'mensaje enviado', 200
    except Exception as e:
        print('Error en la solicitud:', str(e))
        return e, 403


def text_Message(number,text):
    data = json.dumps(
            {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": text
                }
            }
    )
    return data

def administrar_chatbot(text, messageId, name, number):
    text = text.lower() #Mensaje enviado por el usuario
    list = []
    
    data = text_Message(number, 'Hola mundo desde python!')
    enviar_Mensaje_whatsapp(data)