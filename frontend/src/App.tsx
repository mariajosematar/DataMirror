import React from 'react';

async function interact() {
  const response = await fetch('http://localhost:8000/interact', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ type: 'tap', position: 'center' })
  });
  const data = await response.json();
  document.getElementById('reflection')!.innerText = `Próxima vista: ${data.next_view}`;
}

async function askAssistant() {
  const response = await fetch('http://localhost:8000/ask_assistant', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: 'resumen de mi actividad en redes sociales' })
  });
  const data = await response.json();
  document.getElementById('reflection')!.innerText = data.response;
}

async function getFuturePrediction() {
  const response = await fetch('http://localhost:8000/future_prediction');
  const data = await response.json();
  document.getElementById('reflection')!.innerText = `Tendencia en redes sociales: ${data.social_media_trend}, Pronóstico de email: ${data.email_activity_forecast}`;
}

const App: React.FC = () => (
  <div>
    <h1>DataMirror 2.0</h1>
    <div id="mirror">
      <h2>Espejo Digital</h2>
      <p id="reflection">Tu reflejo digital aparecerá aquí.</p>
      <button onClick={interact}>Interactuar</button>
      <button onClick={askAssistant}>Preguntar al Asistente</button>
      <button onClick={getFuturePrediction}>Ver Predicción Futura</button>
    </div>
  </div>
);

export default App;