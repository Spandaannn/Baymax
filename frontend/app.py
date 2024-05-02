from flask import Flask, render_template, Response
import subprocess

app = Flask(__name__)

def generate_output():
    try:
        process = subprocess.Popen(["python", r"C:\Users\Spandan\Projects\Baymax\backend\backend2.py"],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   bufsize=1,
                                   universal_newlines=True)
        for line in iter(process.stdout.readline, b''):
            yield line.strip() + '<br/>\n'
        for line in iter(process.stderr.readline, b''):
            yield line.strip() + '<br/>\n'
        process.stdout.close()
        process.stderr.close()
        process.wait()
    except Exception as e:
        yield str(e) + '<br/>\n'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    return Response(generate_output(), content_type='text/html')

if __name__ == '__main__':
    app.run(debug=True)
