import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ProfilePage() {
    const [user, setUser] = useState(null);

    useEffect(() => {
        const fetchUser = async () => {
            try {
                const response = await axios.get('http://localhost:8000/users/profile/');
                setUser(response.data);
            } catch (error) {
                console.error(error);
            }
        };
        fetchUser();
    }, []);

    if (!user) {
        return (
            <div className="container text-center mt-5">
                <h1 className="text-4xl font-bold mb-4">Loading...</h1>
            </div>
        );
    }

    return (
        <div className="container text-center mt-5">
            <h1 className="text-4xl font-bold mb-4">Profile</h1>
            <div className="w-100">
                <p className="text-gray-600">Username: {user.username}</p>
                <p className="text-gray-600">Email: {user.email}</p>
                {/* Add more user details as needed */}
            </div>
        </div>
    );
}

export default ProfilePage;
