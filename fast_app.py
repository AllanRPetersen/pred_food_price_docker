from fastapi import FastAPI
import joblib
from tensorflow.keras import models
import requests
from pandas.core.frame import DataFrame
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

nn_model = models.load_model('raw_data/neural_network_v1.h5')
preproc = joblib.load('raw_data/preprocessor_v1.joblib')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def index():
    return {"Buenos Dias": True}


@app.get("/predict/")
def predict(value, portion_size, protein, fat, carb, sugar, sodium, calcium,
            kcal, category, index_2019):

    list_of_inputs = {
        'pt_name': [value],
        'protein': [(float(protein) / float(portion_size)) * 1000],
        'fat': [(float(fat) / float(portion_size)) * 1000],
        'carb': [(float(carb) / float(portion_size)) * 1000],
        'sugar': [(float(sugar) / float(portion_size)) * 1000],
        'sodium': [(float(sodium) / float(portion_size)) * 1000],
        'calcium': [(float(calcium) / float(portion_size)) * 1000],
        'kcal': [(float(kcal) / float(portion_size)) * 1000],
        'category': [category],
        '2019': [float(index_2019)]
    }
    inputs = pd.DataFrame.from_dict(list_of_inputs)

    scaled_inputs = preproc.transform(inputs)

    prediction = nn_model.predict(scaled_inputs)

    prediction_1 = prediction[0][0].tolist()

    #response = {'Prediction': prediction_1}

    return prediction_1
