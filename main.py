import os
import joblib
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'model', 'house_prediction_in_cracow.pkl')

if __name__ == "__main__":
    print("test")