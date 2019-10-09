from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Developed by: Warewolves'

@app.route('/func1', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username)
    print(password)
    return 'working!!'

if __name__ == '__main__':
    app.run()
