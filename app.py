from flask import Flask

app = Flask(__name__)

@app.route('/')
def router_one():
    return "Hello World from Router One!"

@app.route('/router-two')
def router_two():
    return "Hello World from Router Two!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run on all interfaces, port 5000