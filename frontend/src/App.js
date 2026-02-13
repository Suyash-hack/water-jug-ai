import React, { useState } from "react";

function App() {
  const [steps, setSteps] = useState([]);
  const [loading, setLoading] = useState(false);

  const solveWaterJug = async () => {
    setLoading(true);
    const response = await fetch("http://127.0.0.1:8000/api/water-jug/");
    const data = await response.json();
    setSteps(data.solution);
    setLoading(false);
  };

  return (
    <div style={{ textAlign: "center", padding: "40px" }}>
      <h1>AI Mini Project – Water Jug Problem</h1>
      <h3>Uninformed Search (BFS)</h3>

      <button
        onClick={solveWaterJug}
        style={{ padding: "10px 20px", fontSize: "16px" }}
      >
        Solve Problem
      </button>

      {loading && <p>Solving...</p>}

      <div style={{ marginTop: "30px" }}>
        {steps.map((step, index) => (
          <p key={index}>
            Step {index}: Jug 1 = {step[0]}L , Jug 2 = {step[1]}L
          </p>
        ))}
      </div>
    </div>
  );
}

export default App;
