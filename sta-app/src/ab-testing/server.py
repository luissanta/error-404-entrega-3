from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hola mundo'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5432, debug=True)