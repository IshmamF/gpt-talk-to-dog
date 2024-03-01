import React, {useState, useEffect} from "react";
import OpenAI from "openai";

export default function Record() {
    var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    var SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList
    const recognition = new SpeechRecognition();

    const [transcription, setTranscription] = useState('') //states
    const [answer, setAnswer] = useState('')

    useEffect(()=>{ //fetch whenever the transcription state updates...
        const request_url = 'http://127.0.0.1:5000/gptanswer';
        const request_param = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: transcription }), // Ensure your backend expects a JSON object with a `question` field
        };
        fetch(request_url, request_param)
            .then(res => res.json())
            .then(ans => setAnswer(ans.answer))
            .catch(err => console.error(`there was an error ${err}`))
    }, [transcription])


    if (SpeechGrammarList) {
        var speechRecognitionList = new SpeechGrammarList();
        recognition.grammars = speechRecognitionList;
    }

    recognition.grammars = speechRecognitionList;
    recognition.continuous = false;
    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

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

    console.log(transcription)
    return (
        <>
            <center>
                <button style={{background:"pink", borderRadius:0.5}} onClick={handleClick}>Record</button>
                <br/>
                <p>Trasncription: {transcription}</p>
                <p>GPT response: <br/>{answer}</p>
            </center>
        </>
    )


}