import { useEffect, useState } from 'react'
import {
  getHealth,
  type HealthResponse,
} from '../shared/api/health'

function App() {
  const [health, setHealth] = useState<HealthResponse | null>(null)
  const [error, setError] = useState<string | null>(null)
  useEffect(() => {
    getHealth()
      .then(setHealth)
      .catch((err: Error) => {
        setError(err.message)
      })
  }, [])
  return (
    <main>
      <h1>Financial AI Agent</h1>
      {error && (
        <p>Backend error: {error}</p>
      )}
      {!health && !error && (
        <p>Checking backend...</p>
      )}
      {health && (
        <div>
          <p>Service: {health.service}</p>
          <p>Status: {health.status}</p>
          <p>Version: {health.version}</p>
          <p>Database: {health.database}</p>
          <p>Migrations: {health.migrations}</p>
        </div>
      )}
    </main>
  )
}

export default App