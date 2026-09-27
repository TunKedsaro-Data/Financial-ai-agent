export type HealthResponse = {
    status: string
    service: string
    version: string
    database: string
    migrations: number
  }
  
  export async function getHealth(): Promise<HealthResponse> {
    const response = await fetch('/api/health')
  
    if (!response.ok) {
      throw new Error(`Health request failed: ${response.status}`)
    }
  
    return response.json()
  }