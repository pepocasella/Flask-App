

from flask import Flask
from flask import request
from datetime import datetime

from AppUtils.functions import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    now = datetime.now()
    return 'Hello from Flask, by Insper DS! - ' + str(now)

@app.route('/core')
def core():
    now = datetime.now()
    return 'Vai Corinthians!! - ' + str(now) 

@app.route('/add/<a>/<b>')
def add(a, b):
    return str(float(a) + float(b))

@app.route('/area')
def myarea():
  altura = request.args.get('altura', default = 0, type = float)
  largura = request.args.get('largura', default = 0, type = float)
  comprimento = request.args.get('comprimento', default = -1, type = float)
  
  if (comprimento < 0):
        return str(altura*largura)
  else:
        return str(altura*largura*comprimento)

@app.route('/query/<text>')
def query(text):
    return ddgquery(text)
    
@app.route('/bitcoins')
def btc():
    return bitcoins()
    
@app.route('/ethereum')
def ether():
    return ethereum()
    
@app.route('/weather/<lat>/<lon>')
def weather(lat, lon):
    return weather(lat, lon)
            

if __name__ == '__main__':
   app.run()