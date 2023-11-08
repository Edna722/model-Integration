import React from 'react';
import './App.css';
import PredictionForm from './components/PredictionForm';
import PredictionResults from './components/PredictionResults';

function App() {
  return (
    <div className="App">
      <h1>Prediction App</h1>
      <PredictionForm />
      <PredictionResults />
    </div>
  );
}

export default App;
