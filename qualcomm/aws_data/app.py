from flask import Flask

# create an app 
app = Flask(__name__)

#decorate the function with route method from app
@app.route("/",methods=['GET','POST'])
def main():
    return "Hello world from Flask"

@app.route("/predict",methods=['GET','POST'])
def main2():
    return "welcome to the prediction page"


if __name__=="__main__":
    app.run(port=5000,host="0.0.0.0")