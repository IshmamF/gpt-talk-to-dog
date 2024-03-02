import Navbar from '../components/navbar'
import React, { useState } from "react";
import Record from '../components/record'

export default function SpeechPrompt() {
    return (
        <div>
            <Navbar/>
            <div className="App">
                <div>
                    {/* auto play needs to be fixed here as chrome doesn't support aotuplay (safari does)*/}
                </div>
            </div>  
            <Record/>
        </div>
    );
}