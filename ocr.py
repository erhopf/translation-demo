import os, requests, uuid, json

if 'COMPUTER_VISION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_KEY']
else:
    print('Environment variable for COMPUTER_VISION_KEY is not set.')
    exit()

def get_ocr(url):
    image_url = url
    base_url = 'https://westus.api.cognitive.microsoft.com/'
    path = 'vision/v2.0/ocr'
    params = {
        'language': 'unk',
        'detectOrientation': 'true',
    }
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = {
        "url" : image_url
    }
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response
