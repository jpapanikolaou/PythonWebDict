from flask import Flask

app = Flask(__name__)#creates instance of 'Flask' class, stored in var app. __name__ sets root path of app. __name__ will specify the module that it is called in.
                    #if we're not importing something, this means that __name__ will be set equal to __main__

@app.route('/')#this is called a 'decorator'. This means that when we hit the root URL '/', we execute hello()
def hello():
    return 'Hello, World!'

@app.route('/api/hello',methods=['GET'])
def api_hello():
    print("Hello world")
    return{'message':"Hello from the API"}

