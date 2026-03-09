# Chat Application

## Overview
A multi-client TCP chat application with a server that enables real-time messaging between multiple users as the group chat.

## Features
- Multi-client support (up to 10 simultaneous connections)
- Join/leave notifications
- Clean exit with `/quit` command

## Requirements
- Standard socket library
- threading library

## Project Structure
```
chat-app/
├── server.py          # Chat server
├── client.py          # Chat client
├── README.md          # This file
└── Report.pdf         # Technical report
```

## Installation
Python3 


## Usage

### Starting the Server
```bash
python3 server.py
```
### Starting a Client
```bash
python3 client.py
```

1. Enter your username when prompted
2. Type messages and press Enter to send
3. Type `/quit` to exit


```python
HOST = '127.0.0.1'  # Server IP address
PORT = 5000          # Server port
LISTENER_LIMIT = 10  # Max concurrent clients
```

## Troubleshooting

**"Address already in use"**
- Wait 30 seconds or change PORT number
- Server uses SO_REUSEADDR to handle this

**"Connection refused"**
- Ensure server is running first
- Check HOST and PORT match in both files

**"Messages not appearing"**
- Check network connection
- Restart both server and clients
