from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Developed by: Warewolves'

@app.route('/func1', methods=['GET', 'POST'])
def func1():
    p1 = request.args.get('p1')
    p2 = request.args.get('p2')
    data = {{'p1':p1 },{'p2':p2}}
    return jsonify(data)
    

if __name__ == '__main__':
    app.run()
