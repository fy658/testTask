from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        # Dictionary to store active connections, with usernames as keys and WebSocket objects as values
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, username: str):
        # Accept the WebSocket connection
        await websocket.accept()
        # Add the connection to the dictionary of active connections
        self.active_connections[username] = websocket
        # Broadcast a message to all clients that a new user has joined
        await self.broadcast(f"System: {username} has joined the chat.")

    def disconnect(self, username: str):
        # Remove the connection from the dictionary of active connections
        del self.active_connections[username]

    async def broadcast(self, message: str):
        # Send the message to all connected clients
        for connection in self.active_connections.values():
            await connection.send_text(message)

    async def send_personal_message(self, message: str, username: str):
        # Send a message to a specific user
        await self.active_connections[username].send_text(message)


# Create an instance of the ConnectionManager
manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    # Connect the new client
    await manager.connect(websocket, username)
    try:
        while True:
            # Wait for messages from the client
            data = await websocket.receive_text()
            # Broadcast the received message to all clients, prepending the sender's username
            await manager.broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        # Handle client disconnection
        manager.disconnect(username)
        # Inform other clients that this user has left
        await manager.broadcast(f"System: {username} has left the chat.")


@app.get("/")
async def get():
    # A simple endpoint to confirm the server is running
    return {"message": "WebSocket chat server is running. Connect to the WebSocket endpoint at /ws/{username}"}