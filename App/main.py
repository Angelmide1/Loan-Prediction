#main.py
import pickle
import pandas as pd
# load saved loan_prediction_model
def load_model():
    with open('loan_prediction_problem_model.pkl', 'rb') as file:
        model = pickle.load(file)
        return model
    
    
    #preprocessing function
    def preprocess(input_data):
        df = pd.DataFrame(input_data, index=[0])
        return df
    
    #prediction function
    def predict(model, input_data):
        processed_data = preprocess(input_data)
        prediction= model.predict(processed_data)
        return prediction