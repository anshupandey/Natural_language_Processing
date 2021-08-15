from flask import Flask,request, render_template
import joblib
import json

vec = joblib.load('vectorizer.pkl')
model = joblib.load('sentiment_model.pkl')

# create an app 
app = Flask(__name__)

#decorate the function with route method from app
@app.route("/",methods=['GET','POST'])
def main():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def main2():
    data = request.form
    data = dict(data) # converting to dictionary
    print(data,type(data))
    data2 = vec.transform([data['data']])
    pred = model.predict(data2)
    print(pred)
    data['prediction'] = pred.tolist()
    #data = json.dumps(data)
    return render_template("output.html",output=data)


if __name__=="__main__":
    app.run(port=5000)