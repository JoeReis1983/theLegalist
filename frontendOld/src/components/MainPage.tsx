import React from 'react';
import { Sidebar } from './Sidebar';
const MainPage: React.FC = () => {
    return (
    <div>
        <Sidebar />
        <h1>Welcome to the Main Page</h1>
        <p>This is the main page of our application.</p>
    </div>
    );
};
export default MainPage;