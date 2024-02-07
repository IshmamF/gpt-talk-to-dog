import { Link } from 'react-router-dom';

export default function Button({routepath, text}) {
    return (
        <div className='m-4'> {/* Adjust margin for better spacing */}
            <Link to={routepath}>
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:scale-105 shadow-lg">
                    {text}
                </button>
            </Link>
        </div>
    );
}
