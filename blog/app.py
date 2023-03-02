from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    username = request.args.get("username")
    method = request.method
    if username:
        return f'Welcome, {username}'
    return f'Welcome to Home Page! Method = {method}'

@app.errorhandler(404)
def handler_404(error):
    return 'Page not found'