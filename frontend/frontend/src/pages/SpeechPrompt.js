import Navbar from '../components/navbar'
import axios from "axios";
import React, { useState } from "react";
    

export default function SpeechPrompt() {


    const request_param = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question: "tell me something funny"}), // Ensure your backend expects a JSON object with a `question` field
    };
    fetch("http://127.0.0.1:5000/gptspeakanswer", request_param)
        .then(res => res.json())
        .then(out => console.log(out))
        .catch(err => console.log(err))

    return (
        <div>
            <Navbar/>
            <div className="App">
                <div>
                    <audio id="audio" controls autoPlay src={'http://127.0.0.1:5000/gptspeakanswer'} />
                    {/* auto play needs to be fixed here as chrome doesn't support aotuplay (safari does)*/}
                </div>
            </div>  
        </div>
    );
}