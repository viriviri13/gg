from flask import Flask, request, make_response
from collections import defaultdict

app = Flask(__name__)

request_data = defaultdict(int)

@app.before_request
def check_request():
    ip = request.remote_addr
    request_data[ip] += 1

@app.route('/')
def home():
    ip = request.remote_addr
    current_requests = request_data[ip]
    response = make_response(f"{current_requests} requests")
    response.headers['Refresh'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
