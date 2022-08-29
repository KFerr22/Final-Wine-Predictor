import os
import pandas as pd
from flask import (
    Flask,
    render_template, 
    redirect, 
    jsonify,
    request)

# import new_wine_predictor
from ml import ML


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict_new_wine")
def predict_new_wine():
    # new_wine_predictor
    return render_template("predict_new_wine.html")        

# Query the database and send the jsonified results
@app.route("/send", methods=["POST"])
def send():
    fixed_acidity = request.form["fixed_acidity"]
    volatile_acidity = request.form["volatile_acidity"]
    citric_acid = request.form["citric_acid"]
    residual_sugar = request.form["residual_sugar"]
    chlorides = request.form["chlorides"]
    free_sulfur_dioxide = request.form["free_sulfur_dioxide"]
    total_sulfur_dioxide = request.form["total_sulfur_dioxide"]
    density = request.form["density"]
    pH = request.form["pH"]
    sulphates = request.form["sulphates"]
    alcohol = request.form["alcohol"]

    wine_data = {
        "fixed acidity": [fixed_acidity],
        "volatile acidity": [volatile_acidity],
        "citric acid": [citric_acid],
        "residual sugar": [residual_sugar],
        "chlorides": [chlorides],
        "free sulfur dioxide": [free_sulfur_dioxide],
        "total sulfur dioxide": [total_sulfur_dioxide],
        "density": [density],
        "pH": [pH],
        "sulphates": [sulphates],
        "alcohol": [alcohol]
    }
        
    model = ML()
    
    prediction = model.predict(wine_data)
        
    return render_template("predict_new_wine.html", result=prediction[0][0])

@app.route("/tableau_viz1")
def tableau_viz():
     return render_template("tableau_viz1.html")

@app.route("/tableau_viz2")
def tableau_viz2():
     return render_template("tableau_viz2.html")

@app.route("/tableau_viz3")
def tableau_viz3():
     return render_template("tableau_viz3.html")


if __name__ == "__main__":
    app.run(debug=True)

