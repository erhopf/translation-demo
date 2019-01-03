$(function() {
  //Translate text with flask route
  $("#translate").on("click", function(e) {
    e.preventDefault();
    var translateVal = document.getElementById("text-to-translate").value;
    var languageVal = document.getElementById("select-language").value;

    if (translateVal !== "") {
      $.ajax({
        url: '/translate-text?text=' + translateVal + '&to=' + languageVal,
        method: 'get',
        success: function(data) {
          for (var i = 0; i < data.length; i++) {
            document.getElementById("translation-result").textContent = data[i].translations[0].text;
            document.getElementById("detected-language-result").textContent = data[i].detectedLanguage.language;
            if (document.getElementById("detected-language-result").textContent !== ""){
              document.getElementById("detected-language").style.display = "block";
            }
            document.getElementById("confidence").textContent = data[i].detectedLanguage.score;
          }
        console.log(document.getElementById("detected-language-result").innerHTML);
        console.log("zip");
        console.log(document.getElementById("translation-result").value);
        }
      });
    };
  });
  // Convert text-to-speech
  $("#text-to-speech").on("click", function(e) {
    e.preventDefault();
    var ttsInput = document.getElementById("translation-result").value;
    var ttsVoice = document.getElementById("select-voice").value;
    var xhr = new XMLHttpRequest();
    xhr.open("GET", '/text-to-speech?text=' + ttsInput + '&voice=' + ttsVoice, true);
    xhr.responseType = "blob";
    xhr.onload = function(evt){
      if (xhr.status === 200) {
        audioBlob = new Blob([xhr.response], {type: "audio/mpeg"});
        audioURL = URL.createObjectURL(audioBlob);
        if (audioURL.length > 5){
          var audio = document.getElementById('audio');
          var source = document.getElementById('audio-source');
          source.src = audioURL;
          audio.load();
          audio.play();
        }else{
          console.log("An error occurred getting and playing the audio.")
        }
      }
    }
    xhr.send();
  });

  //Run sentinment analysis on input and translation.
  $("#sentiment-analysis").on("click", function(e) {
    e.preventDefault();
    var inputText = document.getElementById("text-to-translate").value;
    var inputLanguage = document.getElementById("detected-language-result").innerHTML;
    var outputText = document.getElementById("translation-result").value;
    var outputLanguage = document.getElementById("select-language").value;
    if (inputText !== "") {
      $.ajax({
        url: '/sentiment-analysis?input=' + inputText + '&inlang=' + inputLanguage + '&output=' + outputText + '&outputlang=' + outputLanguage,
        method: 'get',
        success: function(data) {
          console.log(data);
          document.getElementById("input-sentiment").textContent = data.documents[0].score;
          if (typeof data.documents[1] !== 'undefined') {
            document.getElementById("translation-sentiment").textContent = data.documents[1].score;
          } else{
            document.getElementById("translation-sentiment").textContent = "Sentiment analysis isn't supported for " + document.getElementById("select-language").value + "."
          }
          if (document.getElementById("input-sentiment").textContent !== '' && document.getElementById("translation-result").textContent !== ''){
            document.getElementById("sentiment").style.display = "block";
          }
        }
      });
    }
  });
  // Automatic voice font selection based on translation output.
  $('select[id="select-language"]').change(function(e) {
    if ($(this).val() == "en"){
      document.getElementById("select-voice").value = "(en-US, Jessa24kRUS)";
    }
    if ($(this).val() == "fr"){
      document.getElementById("select-voice").value = "(fr-FR, HortenseRUS)";
    }
    if ($(this).val() == "de"){
      document.getElementById("select-voice").value = "(de-DE, HeddaRUS)";
    }
    if ($(this).val() == "it"){
      document.getElementById("select-voice").value = "(it-IT, LuciaRUS)";
    }
    if ($(this).val() == "ja"){
      document.getElementById("select-voice").value = "(ja-JP, HarukaRUS)";
    }
    if ($(this).val() == "es"){
      document.getElementById("select-voice").value = "(es-ES, HelenaRUS)";
    }
    if ($(this).val() == "tr"){
      document.getElementById("select-voice").value = "(tr-TR, SedaRUS)";
    }
    if ($(this).val() == "vi"){
      document.getElementById("select-voice").value = "(vi-VN, An)";
    }
  });
});
