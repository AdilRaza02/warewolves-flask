from flask import Flask, request, jsonify
import test

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Developed by: Warewolves'

@app.route('/func1', methods=['GET', 'POST'])
def func1():
    re=test.get_cleaned_data()
    print(re)
    return (re)
    

if __name__ == '__main__':
    app.run()
