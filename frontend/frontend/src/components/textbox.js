import {useState} from 'react';

export default function TextBox () {
    const [answer, setAnswer] = useState(''); // Used for storing the user input
    const [output, setOutput] = useState(''); // Corrected to useState, used for storing the response
    const [isLoading, setIsLoading] = useState(false);

    async function handleOnSubmit() {
        setIsLoading(true);
        // Assuming `answer` contains the user's question, and you want to send this to the backend
        const request_url = 'http://127.0.0.1:5000/gptanswer';
        const request_param = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: answer }), // Ensure your backend expects a JSON object with a `question` field
        };
        const response = await fetch(request_url, request_param);
        const responseData = await response.json();
        
        setOutput(responseData.answer); // Assuming the backend response contains an `answer` field
        setIsLoading(false);
    }

    const handleChange = (event) => {
        setAnswer(event.target.value);
    };

    return (
        <div className="flex flex-col justify-between px-4 py-2">
            {/* Input section centered */}
            <div className="mt-7 flex flex-col justify-center items-center space-y-2">
                <label htmlFor="textInput" className="text-lg font-semibold">What would you like help with:</label>
                <div className='flex items-center space-x-2'>
                    <input
                        type="text"
                        id="textInput"
                        value={answer}
                        onChange={handleChange}
                        className="border border-gray-300 p-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                        placeholder="Enter your question"
                    />
                    <button 
                        onClick={handleOnSubmit}
                        className='bg-blue-500 rounded p-2 text-white hover:bg-blue-700 font-bold transition duration-300 ease-in-out transform hover:scale-105 shadow-lg'
                        disabled={isLoading}
                    >
                        {isLoading ? 'Loading...' : 'Submit'}
                    </button>
                </div>
            </div>
            {/* Responses section with answer on the right and output on the left */}
            <div className="mt-10">
                {answer && output && (
                <div className="text-right">
                    <p className="inline-block bg-blue-500 rounded p-2 text-white">{answer}</p>
                </div>
                )}
                {output && (
                <div className="text-left mt-2"> {/* Added mt-2 for a little space between the answer and output */}
                    <p className="inline-block bg-gray-200 rounded p-2">{output}</p>
                </div>
                )}
            </div>
        </div>
    );
    
}
