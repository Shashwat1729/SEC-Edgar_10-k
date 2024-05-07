import React, { useState } from 'react';
import axios from 'axios';

const TextAnalysis = () => {
    const [text, setText] = useState('');
    const [insight, setInsight] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/', { text });
            setInsight(response.data.insight);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h1>Text Analysis App</h1>
            <form onSubmit={handleSubmit}>
                <textarea value={text} onChange={(e) => setText(e.target.value)} rows="10" cols="50"></textarea><br />
                <input type="submit" value="Submit" />
            </form>
            {insight && <p>Insight: {insight}</p>}
        </div>
    );
};

export default TextAnalysis;
