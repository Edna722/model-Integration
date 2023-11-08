import React, { useState } from 'react';
import axios from 'axios';

function PredictionForm() {
  const [data, setData] = useState({}); // State to hold form data

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/predict', data);
      console.log(response.data); // Handle the prediction response
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Add form input fields */}
    </form>
  );
}

export default PredictionForm;
