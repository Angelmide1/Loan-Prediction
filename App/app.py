#app.py
from sklearn.metrics import PredictionErrorDisplay
import streamlit as st
from App.main import load_model, predict


# load model
model = load_model()

#streamlit app layout
st.title("Loan prediction Application")

#user input fields
st.header("Enter the following details to predict loan approval:")

#input fields for the user (adjust these as per your model's features)
gender = st.selectbox("Gender", ['Male', "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
income = st.number_input("Applicant's Income", min_value =0)
loan_amount = st.number_input("Loan Amount", min_value = 0)
loan_term = st.number_input("Loan Term(in months)", min_value = 0)
credit_history = st.selectbox("Credit History", [0,1])

#organizing input data into a dictionary
input_data = {
    "Gender": gender,
    "Married": married,
    "Dependents": dependents,
    "Income": income,
    "LoanAmount": loan_amount,
    "Loan_Amount_Term": loan_term,
    "Credit_History": credit_history
}

#Button for prediction
if st.button("Predict Loan Status"):
    prediction = Predict (model, input_data) # type: ignore
    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Not Approved")