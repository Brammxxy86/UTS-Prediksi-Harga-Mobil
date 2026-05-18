from flask import Flask,render_template,request
import joblib
import numpy as np

app=Flask(__name__)

model=joblib.load(
"../models/model_mobil.pkl"
)

@app.route(
"/",
methods=["GET","POST"]
)

def home():

    hasil=None

    if request.method=="POST":

        umur=float(
        request.form["umur"]
        )

        km=float(
        request.form["km"]
        )

        fuel=float(
        request.form["fuel"]
        )

        transmisi=float(
        request.form["transmisi"]
        )

        engine=float(
        request.form["engine"]
        )

        power=float(
        request.form["power"]
        )

        seats=float(
        request.form["seats"]
        )


        data=np.array([[

        umur,
        km,
        fuel,
        transmisi,
        engine,
        power,
        seats

        ]])

        pred=model.predict(data)

        hasil="₹ {:,}".format(
        int(pred[0])
        )

    return render_template(
    "index.html",
    hasil=hasil
    )


if __name__=="__main__":

    app.run(debug=True)