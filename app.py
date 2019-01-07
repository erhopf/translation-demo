from flask import Flask, render_template, url_for, jsonify, request
import translate, synthesize, sentiment, sys
if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    #Old get request
    #text_input = request.args.get('text', default='', type=str)
    #translation_output = request.args.get('to', default='', type=str)
    response = translate.get_translation(text_input, translation_output)
    return jsonify(response)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text_input = data['text']
    voice_font = data['voice']
    #Old get request
    #text_input = request.args.get('text', default='', type=str)
    #voice_font = request.args.get('voice', default='', type=str)
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
