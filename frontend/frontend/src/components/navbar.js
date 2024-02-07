import React from 'react';
import { Link } from 'react-router-dom';

export default function Navbar() {
    return(
        <nav className='bg-black flex justify-between items-center p-3'>
            <Link to='/' className='text-white text-xl'>
                SPOT TTS
            </Link>
            <ul className="flex space-x-4">
                <li>
                    <Link to='/textprompt' className="text-white hover:text-gray-300">Text Prompt</Link>
                </li>
                <li>
                    <Link to='/speechprompt' className="text-white hover:text-gray-300">Speech Prompt</Link>
                </li>
                <li>
                    <Link to='/imageprompt' className="text-white hover:text-gray-300">Image Prompt</Link>
                </li>
                <li>
                    <Link to='/speak' className="text-white hover:text-gray-300">Speak</Link>
                </li>
            </ul>
        </nav>
    );
}