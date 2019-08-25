from flask import *

app=Flask(__name__)

@app.route('/name/<fname>')
def home(fname):
    return "<h3>Hello "+fname+"</h3>"

@app.route('/index')
def index():
    return render_template('index.html',name='Bratati')

@app.route('/login')
def start():
    return render_template('login.html')

@app.route('/success',methods=['POST'])
def login():
    if request.method=="POST":
        data=request.form
        print(data['uname'])
        print(data['upass'])
        return "OK"


if __name__=='__main__':
    app.run(debug=True,port=6530)