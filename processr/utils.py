import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "Iris Setosa", 1: "Iris Versicolour", 2: "Iris Virginica"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
            "alcohol": d.alcohol,
            "malic_acid": d.malic_acid,
            "ash": d.ash,
            "alcalinity_of_ash": d.alcalinity_of_ash,
            "magnesium": d.magnesium,
            "total_phenols": d.total_phenols,
            "flavanoids": d.flavanoids,
            "nonflavanoid_phenols": d.proanthocyanins,
            "color_intensity": d.color_intensity,
            "hue": d.hue,
            "od280_od315_of_diluted_wines": d.od280_od315_of_diluted_wines,
            "proline": d.proline,
        }
        for d in data
    ]

    return processed
