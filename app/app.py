from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_html():
    return send_from_directory('static', 'sample.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
