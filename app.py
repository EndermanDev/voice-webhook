from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
commands = []  # Store commands in memory

@app.route('/webhook', methods=['POST'])
def receive_command():
    data = request.form.get('trigger')
    if data:
        command_id = str(uuid.uuid4())
        commands.append({'uuid': command_id, 'content': data})
        return jsonify({'status': 'success', 'uuid': command_id}), 200
    return jsonify({'status': 'error', 'message': 'No trigger provided'}), 400

@app.route('/webhook', methods=['GET'])
def get_commands():
    return jsonify(commands)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
