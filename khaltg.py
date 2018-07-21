from flask import Flask, render_template
import random
app = Flask(__name__)
@app.route("/")
def num():
	return render_template("khaled.html")


if __name__ == "__main__":
	app.run(port = 3000, debug= True)
	