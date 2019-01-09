# Translate, synthesize, and analyze text with Azure

This is a simple web application built using Flask with a sprinkling of jQuery, Bootstrap, and vanilla HTML5.
The goal is to demonstrate how a developer may use different Cognitive Services together to create a delightful
experience for customers.

In this app we're using text translation, sentiment analysis, and text-to-speech. [Test it out!](https://translator-tts-demo.azurewebsites.net/)

## Prerequisites

If you clone/fork this repository for personal use, you'll need subscription keys for these Cognitive Services:

* Speech Services
* Translator Text
* Text Analytics

*This app works with trial subscriptions.*

After you've obtained the keys, you'll need to set some environment variables. This app looks for these env variables:

* `SPEECH_SERVICE_KEY`
* `TRANSLATOR_TEXT_KEY`
* `TEXT_ANALYTICS_KEY`
