import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<!DOCTYPE html><html><p> Its alive </p></html>'
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port, debug=True) #creates server waiting for a hit of the address and routes its to matching 