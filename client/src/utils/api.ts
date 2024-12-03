import { History } from "./types"

export const getHistory = async (session: string = "default"): Promise<History[]> => {
    const response = await fetch(`http://localhost:8000/history?session_id=${session}`)
    const output = await response.json()
    console.log(output)
    return output.data
}

export const sendMessage = async (session: string = "default", query: string): Promise<boolean> => {
    const response = await fetch(`http://localhost:8000/query?query=${encodeURIComponent(query)}&session_id=${session}`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    });
    return response.status == 200
}