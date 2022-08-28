from collections import namedtuple
# from sklearn.linear_model import LogisticRegression
import os
import pandas as pd
from flask import (
    Flask,
    render_template, 
    redirect, 
    jsonify,
    request)

# from pathlib import Path

# import new_wine_predictor
from ml import ML

# import tempfile

app = Flask(__name__)

# # Use flask_pymongo to set up mongo connection
# # app.config["MONGO_URI"] = "mongodb://localhost:27017/internetspeeds"
# # mongo = PyMongo(app)

# from flask_sqlalchemy import SQLAlchemy

# uri = os.getenv("DATABASE_URL","")
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://","postgresql://",1)
# app.config['SQLALCHEMY_DATABASE_URI'] = uri or "sqlite:///db.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class Wine(db.Model):
#     __tablename__ = 'wine'

#     id = db.Column(db.Integer, primary_key=True)
#     fixed_acidity = db.Column(db.Integer)
#     volatile_acidity = db.Column(db.Integer)
#     citric_acid = db.Column(db.Integer)
#     residual_sugar = db.Column(db.Integer)
#     chlorides = db.Column(db.Integer)
#     free_sulfur_dioxide = db.Column(db.Integer)
#     total_sulfur_dioxide = db.Column(db.Integer)
#     density = db.Column(db.Integer)
#     pH = db.Column(db.Integer)
#     sulphates = db.Column(db.Integer)
#     alcohol = db.Column(db.Integer)

#     def __repr__(self):
#         return '<Wine %r>' % (self.name)

@app.route("/")
def index():
    #scrape_data.scrape_info()
    #internet_data = mongo.db.countryspeed.find_one()
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


    # wine_dict = {
    #     "fixed_acidity": fixed_acidity,
    #     "volatile_acidity": volatile_acidity,
    #     "citric_acid": citric_acid,
    #     "residual_sugar": residual_sugar,
    #     "chlorides": chlorides,
    #     "free_sulfur_dioxide": free_sulfur_dioxide,
    #     "total_sulfur_dioxide": total_sulfur_dioxide,
    #     "density": density,
    #     "pH": pH,
    #     "sulphates": sulphates,
    #     "alcohol": alcohol
    # }
    # wine_df = pd.from_dict(wine_dict)

    '''
    wine = Wine(fixed_acidity=fixed_acidity, volatile_acidity=volatile_acidity, citric_acid=citric_acid, residual_sugar=residual_sugar, chlorides=chlorides, free_sulfur_dioxide=free_sulfur_dioxide, total_sulfur_dioxide=total_sulfur_dioxide, density=density, pH=pH, sulphates=sulphates, alcohol=alcohol)
    db.session.add(wine)
    db.session.commit()

    '''
    '''
    temp = tempfile.TemporaryFile(mode="w+t", delete=False)

    keys  = [f"\"{key}\"" for key in wine_data.keys()]
    header = ",".join(keys)
    values = ",".join(wine_data.values())

    '''
        
    model = ML()
    # df = pd.read_csv(Path(csv_filename))
    prediction = model.predict(wine_data)
    #prediction = model.predict("C:\\Users\\Home\\AppData\\Local\\Temp\\tmplb_r0bhk")


    
    return render_template("predict_new_wine.html", result=prediction[0][0])

# @app.route("/api/wine")
# def wine():
#     results = db.session.query(Wine.fixed_acidity, Wine.volatile_acidity, Wine.citric_acid, Wine.residual_sugar, Wine.chlorides, Wine.free_sulfur_dioxide, Wine.total_sulfur_dioxide, Wine.density, Wine.pH, Wine.sulphates, Wine.alcohol).all()

#     fixed_acidity = [result[0] for result in results]
#     volatile_acidity = [result[1] for result in results]
#     citric_acid = [result[2] for result in results]
#     residual_sugar = [result[3] for result in results]
#     chlorides = [result[4] for result in results]
#     free_sulfur_dioxide = [result[5] for result in results]
#     total_sulfur_dioxide = [result[6] for result in results]
#     density = [result[7] for result in results]
#     pH = [result[8] for result in results]
#     sulphates = [result[9] for result in results]
#     alcohol = [result[10] for result in results]

#     wine_data = [{
#         "fixed_acidity": fixed_acidity,
#         "volatile_acidity": volatile_acidity,
#         "citric_acid": citric_acid,
#         "residual_sugar": residual_sugar,
#         "chlorides": chlorides,
#         "free_sulfur_dioxide": free_sulfur_dioxide,
#         "total_sulfur_dioxide": total_sulfur_dioxide,
#         "density": density,
#         "pH": pH,
#         "sulphates": sulphates,
#         "alcohol": alcohol
#     }]

#     return jsonify(wine_data)

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

