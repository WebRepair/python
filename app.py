from flask import Flask, render_template, request, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        command = ['python', 'openAIapi.py', query]
        result = subprocess.run(command, capture_output=True, text=True)
        response = result.stdout
        return render_template('index.html', response=response, query=query)
    else:
        return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

if __name__ == '__main__':
    app.run()
