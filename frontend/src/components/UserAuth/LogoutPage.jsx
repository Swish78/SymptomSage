import React, { useEffect } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';

function LogoutPage() {
    const history = useHistory();

    useEffect(() => {
        const logout = async () => {
            try {
                await axios.post('http://localhost:8000/users/logout/');
                localStorage.removeItem('access_token');
                history.push('/login');
            } catch (error) {
                console.error(error);
            }
        };
        logout();
    }, [history]);

    return (
        <div className="container text-center mt-5">
            <h1 className="text-4xl font-bold mb-4">Logging out...</h1>
        </div>
    );
}

export default LogoutPage;
