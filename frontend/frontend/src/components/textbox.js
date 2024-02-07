import React from 'react';

export default function () {
    const [enteredText, setEnteredText] = useState({
        'textInput': ""
    });
    const [answer, setAnswer] = useEffect(null);
    const [isLoading, setIsLoading] = useState(false);

    async function handleOnSubmit() {
        setIsLoading(true);

        const request_url = 'http://127.0.0.1:5000/gptAnswer';
        const request_param = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(enteredText),
        };
        const response = await fetch(request_url, request_param);
        const responseData = await response.json();
        setAnswer(responseData.answer)
    }


}