import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [status, setStatus] = useState<{status: string; version: string; db: string} | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    axios.get("/api/health")
      .then(res => setStatus(res.data))
      .catch(err => setError(err.message));
  }, []);

  return (
    <div style={{fontFamily: "sans-serif", padding: 24}}>
      <h1>EcoGrid+ Dashboard</h1>
      <p>Verificação de saúde do sistema</p>
      {error && <div style={{color:"red"}}>Erro: {error}</div>}
      {status ? (
        <div style={{border:"1px solid #ccc", padding:16, borderRadius:8, maxWidth: 360}}>
          <div><strong>Status API:</strong> {status.status}</div>
          <div><strong>Versão:</strong> {status.version}</div>
          <div><strong>Banco:</strong> {status.db}</div>
        </div>
      ) : (<div>Carregando...</div>)}
    </div>
  );
}
export default App;