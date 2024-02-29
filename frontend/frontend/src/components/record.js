import React, {useState} from "react";

export default function Record() {
    var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    var SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList
    const recognition = new SpeechRecognition();

    if (SpeechGrammarList) {
        var speechRecognitionList = new SpeechGrammarList();
        recognition.grammars = speechRecognitionList;
    }

    recognition.grammars = speechRecognitionList;
    recognition.continuous = false;
    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    const [transcription, setTranscription] = useState('')

    function handleClick() {
        recognition.start();
    }

    recognition.onspeechend = function() {
        recognition.stop();
    }

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript
        setTranscription(transcript)
    }

    recognition.onerror = function(event) {
        console.error("Speech recognition error detected: " + event.error)
    }

    return (
        <>
            <button onClick={handleClick}>Record</button>
            <br/>
            <p>Trasncription: {transcription}</p>
        </>
    )


}