import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Certifique-se de que esta linha está presente
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
