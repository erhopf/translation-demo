from flask import Flask, render_template, url_for, jsonify, request
import translate, synthesize, sentiment, ocr, sys
if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate-text')
def translate_text():
    text_input = request.args.get('text', default='', type=str)
    translation_output = request.args.get('to', default='', type=str)
    response = translate.get_translation(text_input, translation_output)
    return jsonify(response)

@app.route('/text-to-speech')
def text_to_speech():
    text_input = request.args.get('text', default='', type=str)
    voice_font = request.args.get('voice', default='', type=str)
    tts = synthesize.TextToSpeech(text_input, voice_font)
    tts.get_token()
    audio_response = tts.save_audio()
    return audio_response

@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    input_text = data['inputText']
    input_lang = data['inputLanguage']
    output_text = data['outputText']
    output_lang =  data['outputLanguage']
    response = sentiment.get_sentiment(input_text, input_lang, output_text, output_lang)
    return jsonify(response)

@app.route('/ocr')
def ocr_image():
    image_url = request.args.get('image', default='', type=str)
    response = ocr.get_ocr(image_url)
    return jsonify(response)
