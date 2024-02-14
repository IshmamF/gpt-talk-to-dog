import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import TextPrompt from './pages/TextPrompt'; 
import SpeechPrompt from './pages/SpeechPrompt'; 
import ImagePrompt from './pages/ImagePrompt'; 
import Landing from './pages/LandingPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Landing/>}></Route>
        <Route path="/textprompt" element={<TextPrompt />} />
        <Route path="/speechprompt" element={<SpeechPrompt />} />
        <Route path="/imageprompt" element={<ImagePrompt />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
