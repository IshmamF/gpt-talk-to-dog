import React from "react";
import Navbar from '../components/navbar'
import Button from "../components/button";
import Header from "../components/header";

export default function Landing() {
    return (
        <div>
            <Navbar/>
            <Header/>
            <div className='flex flex-col items-center mt-5'>
                <Button routepath="/textprompt" text="Text Prompt"/>
                <Button routepath="/speechprompt" text="Speech Prompt"/>
                <Button routepath="/imageprompt" text="Image Prompt"/>
                <Button routepath="/speak" text="Speak"/>
            </div>
        </div>
    );
}