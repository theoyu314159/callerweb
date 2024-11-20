from flask import Flask
from flask import request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    html=''
    with open('index.html',"r",encoding="utf-8") as f:
        html = f.read()
    return html
@app.route('/url', methods=['POST'])
def submit():
    html=''
    with open('index.html',"r",encoding="utf-8") as f:
        html = f.read()
    submit = request.form.get('url')
    path=f'{submit}.txt'
    with open( path,'w',encoding="utf-8") as f:
        f.write(str(0))
    k=f'http://192.168.1.109:5000/{path}'
    y=f'http://192.168.1.109:5000/{path}/w'
    out='使用者網址:',k,'控制號碼網址:',y
    return  html.replace('<out/>',str(out))

@app.route('/<string:filen>')
def num(filen):
    html=''
    with open('number.html',"r",encoding="utf-8") as f:
        html = f.read()
    with open(filen,"r",encoding="utf-8") as f:
        out=f.read()
    return  html.replace('<out/>',out)

@app.route('/<string:filen>/w', methods=['GET','POST'])
def back(filen):
    html=''
    with open('back.html',"r",encoding="utf-8") as f:
        html = f.read()
    if request.method == 'POST':
        num=request.form.get('num')
        with open(filen, "w", encoding="utf-8") as f:
                    f.write(num)
    now=''
    with open(filen, "r", encoding="utf-8") as f:
        now=f.read()
    
    return  html.replace('<out/>',now)

app.run(debug=True, host='0.0.0.0')