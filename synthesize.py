import os, requests, time

class TextToSpeech(object):
    def __init__(self, input_text, voice_font):
        if 'SPEECH_SERVICE_KEY' in os.environ:
            subscription_key = os.environ['SPEECH_SERVICE_KEY']
        else:
            print('Environment variable for SPEECH_SERVICE_KEY is not set.')
            exit()
        self.subscription_key = subscription_key
        self.input_text = input_text
        self.voice_font = voice_font
        self.timestr = time.strftime('%Y%m%d-%H%M')
        self.access_token = None

    # This function performs the token exchange.
    def get_token(self):
        fetch_token_url = 'https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken'
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    # This function calls the TTS endpoint with the access token.
    def save_audio(self):
        base_url = 'https://westus.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'YOUR_RESOURCE_NAME',
        }
        body = "<speak version='1.0' xml:lang='en-US'><voice xml:lang='en-US' xml:gender='Female' name='Microsoft Server Speech Text to Speech Voice " + self.voice_font + "'>" + self.input_text + "</voice></speak>"

        response = requests.post(constructed_url, headers=headers, data=body)
        # Write the response as a wav file for playback. The file is located
        # in the same directory where this sample is run.
        print(response)
        return response.content
