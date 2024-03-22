import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import axios from 'axios';
import HomePage from "./components/HomePage.jsx";
import LoginPage from './components/UserAuth/LoginPage';
import LogoutPage from './components/UserAuth/LogoutPage';
import RegisterPage from './components/UserAuth/RegisterPage';
import ProfilePage from './components/UserAuth/ProfilePage';

axios.defaults.baseURL = 'http://localhost:8000/';

function App() {
    return (
        <Router>
            <Switch>
                <Route exact path="/" component={HomePage} />
                <Route path="/login" component={LoginPage} />
                <Route path="/logout" component={LogoutPage} />
                <Route path="/register" component={RegisterPage} />
                <Route path="/profile" component={ProfilePage} />
            </Switch>
        </Router>
    );
}

export default App;