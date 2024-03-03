import React, {useState, useEffect} from "react";
import OpenAI from "openai";

export default function Record() {
    var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    var SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList
    const recognition = new SpeechRecognition();
    const synth = window.speechSynthesis;

    const [transcription, setTranscription] = useState('') //states
    const [gptRes, setGptRes] = useState('')

    useEffect(()=>{ //fetch whenever the transcription state updates...
        // oddly enough it fetches before it needs to so this check is to ensure there is no misfire when we first call it
        // check this over maybe it might be the post method that causes this misfire
        // this shouldn't fire at all on the initial call since it depends on the change of the transcription state...
        if (transcription){ 
            const request_url = 'http://127.0.0.1:5000/gptanswer';
            const request_param = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ question: transcription }), // Ensure your backend expects a JSON object with a `question` field
            };
            fetch(request_url, request_param)
                .then(res => res.json())
                .then(ans => setGptRes(ans.answer))
                .catch(() => setGptRes('There was an internal error please try again later!'))
        }
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

    const utterThis = new SpeechSynthesisUtterance(gptRes);
    const handleSpeakClick = () => synth.speak(utterThis) //repeat what was said

    return (
        <>
            <center>
                <button style={{background:"pink", borderRadius:0.5}} onClick={handleClick}>Record</button>
                <br/>
                <p>Trasncription: {transcription}</p>
                <p>GPT response: <br/>{gptRes}</p>
                {gptRes.length ? null :<button style={{background:"yellow", borderRadius:0.5}} onClick={handleSpeakClick}>repeat</button>}
            </center>
        </>
    )
}