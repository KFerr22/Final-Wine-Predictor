# Wine Quality Machine Learning Prediction Model

import joblib
import pandas as pd

class ML:
    def __init__(self):
        self.new_wine_predictor=joblib.load( 'finalproject_wine.sav')
        self.new_X_scaler=joblib.load('xscaler.sav')

    def predict(self, wine_data):

        new_wine_df = pd.DataFrame(wine_data)
        new_y=self.new_X_scaler.transform(new_wine_df)

        return self.new_wine_predictor.predict(new_y)
      



