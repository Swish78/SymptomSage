import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';

function LoginPage() {
    const history = useHistory();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/users/login/', {
                username,
                password,
            });
            localStorage.setItem('access_token', response.data.access_token);
            history.push('/');
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="container mt-5">
            <h1 className="text-center text-4xl font-bold mb-4">Login</h1>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="username" className="form-label">Username</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        className="form-control"
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="password" className="form-label">Password</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="form-control"
                    />
                </div>
                <button
                    type="submit"
                    className="btn btn-primary w-100"
                >
                    Login
                </button>
            </form>
        </div>
    );
}

export default LoginPage;
