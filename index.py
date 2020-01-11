from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route("/")
def index():
    name = ""
    link = ""
    makeQR(name, link)
    return render_template("index.html")

def makeQR(name, link):
    qr = qrcode.make(name + "のWebサイト -> " + link)
    qr.save('static/result/MySite.png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
