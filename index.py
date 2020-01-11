from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/result", methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		name = request.form['name']
		url = request.form['url']
		makeQR(name, url)
		ResultImg = "../static/result/result.png"
		return render_template("result.html", ResultImg = ResultImg)

def makeQR(name, link):
	qr = qrcode.make(name + "のWebサイト -> " + link)
	qr.save('static/result/result.png')

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)