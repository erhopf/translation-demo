# -*- coding: utf-8 -*-

import os, requests, uuid, json

if 'SENTIMENT_ANALYSIS_KEY' in os.environ:
    subscription_key = os.environ['SENTIMENT_ANALYSIS_KEY']
else:
    print('Environment variable for SENTIMENT_ANALYSIS_KEY is not set.')
    exit()

def get_sentiment(input_text, input_language, output_text, output_language):
    base_url = 'https://westus.api.cognitive.microsoft.com/text/analytics'
    path = '/v2.0/sentiment'
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = {
        "documents":
            [{
                "language":
                    input_language,
                    "id": "1",
                    "text": input_text
            },
            {
                "language":
                output_text,
                "id": "2",
                "text": output_language
            }]
    }
    request = requests.post(constructed_url, headers=headers, json=body)
    response = json.dumps(request.json(), sort_keys=True, ensure_ascii=False, separators=(',', ': '))
    return response
