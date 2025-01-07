from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'POST':
        task = request.json.get('task')
        tasks.append(task)
        return jsonify({'message': 'Task added', 'tasks': tasks}), 201
    return jsonify({'tasks': tasks})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
