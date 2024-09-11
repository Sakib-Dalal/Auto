from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/address')
def address():
    return render_template("address.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)