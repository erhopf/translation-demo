from flask import Flask, render_template, url_for, jsonify, request
import translate, synthesize, sentiment
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate-text')
def translate_text():
    text_input = request.args.get("text", default="", type=str)
    translation_output = request.args.get("to", default="en", type=str)
    response = translate.get_translation(text_input, translation_output)
    return response

@app.route('/text-to-speech')
def text_to_speech():
    text_input = request.args.get("text", default="", type=str)
    voice_font = request.args.get("voice", default="", type=str)
    tts = synthesize.TextToSpeech(text_input, voice_font)
    tts.get_token()
    audio = tts.save_audio()
    return audio

@app.route('/sentiment-analysis')
def sentiment_analysis():
    input_text = request.args.get("input", default="", type=str)
    input_language = request.args.get("inlang", default="", type=str)
    output_text = request.args.get("output", default="", type=str)
    output_language =  request.args.get("outlang", default="", type=str)
    response = sentiment.get_sentiment(input_text, input_language, output_text, output_language)
    return response
