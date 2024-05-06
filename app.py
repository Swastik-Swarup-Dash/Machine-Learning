from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict/', methods = ["Get","Post"])
def predict():
    if request.method == "Post":
        Open = request.form.get("Open")
        High = request.form.get("High")
        Low = request.form.get("Low")
        Volume = request.form.get("Volume")
    prediction = utils.preprocess(Open,High,Low,Volume)
    return render_template('prediction.html',prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)