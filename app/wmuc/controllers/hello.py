from wmuc import app

@app.route('/')
def hello():
    return "Hello World"
