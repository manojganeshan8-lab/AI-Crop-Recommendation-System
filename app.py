from flask import Flask, render_template, request
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load dataset
data = pd.read_csv("tamilnadu_crop_dataset_1000.csv")

data.columns = data.columns.str.strip().str.lower()

X = data[['n','p','k','temperature','humidity','ph','rainfall']]

data['target'] = data['crop'] + " - " + data['place']
y = data['target']

model = RandomForestClassifier()
model.fit(X,y)


@app.route("/", methods=["GET","POST"])
def home():

    crop=None
    place=None

    if request.method=="POST":

        N=float(request.form["nitrogen"])
        P=float(request.form["phosphorus"])
        K=float(request.form["potassium"])
        temp=float(request.form["temperature"])
        humidity=float(request.form["humidity"])
        ph=float(request.form["ph"])
        rainfall=float(request.form["rainfall"])

        prediction=model.predict([[N,P,K,temp,humidity,ph,rainfall]])

        result=prediction[0].split(" - ")

        crop=result[0]
        place=result[1]

        # Save history
        history_data={
            "Place":place,
            "N":N,
            "P":P,
            "K":K,
            "Temperature":temp,
            "Humidity":humidity,
            "pH":ph,
            "Rainfall":rainfall,
            "Crop":crop
        }

        df=pd.DataFrame([history_data])

        if not os.path.exists("history.csv"):
            df.to_csv("history.csv",index=False)
        else:
            df.to_csv("history.csv",mode="a",header=False,index=False)

    return render_template("index.html",crop=crop,place=place)


@app.route("/history")
def history():

    try:
        df=pd.read_csv("history.csv")
        records=df.to_dict(orient="records")
    except:
        records=[]

    return render_template("history.html",records=records)


if __name__=="__main__":
    app.run(debug=True)