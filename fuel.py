import streamlit as st
import pickle as pk
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

with open("model101.pickle", 'rb') as file:
    model = pk.load(file)

st.title('CO2 Emission by Your Vehicle')
st.image('https://www.ledgerinsights.com/wp-content/uploads/2021/10/co2-carbon-emissions-vehicle-car-auto.jpg')
st.header("Enter all values for carbon emission prediction")

# Inputs
engine_size = st.number_input("Engine Size (e.g. 2.0)", 1.0, 10.0, step=0.1)
cylinders = st.number_input("Number of Cylinders", 1, 15)
fuel_consumptions = st.number_input("Fuel Consumption (L/100km)", 1.0, 30.0, step=0.1)
Fuel = st.selectbox("Pick the Fuel Type", ["Type X", "Type Z", "Type D", "Type E", "Type N"])

# Encode Fuel input (ordinal encoding)
fuel_categories = [["Type X", "Type Z", "Type D", "Type E", "Type N"]]
ord_enc = OrdinalEncoder(categories=fuel_categories)
fuel_encoded = ord_enc.fit_transform([[Fuel]])[0][0]

# Build dataframe
df = pd.DataFrame([[engine_size, cylinders, fuel_encoded, fuel_consumptions]],
                  columns=['ENGINE SIZE', 'CYLINDERS', 'FUEL', 'FUEL CONSUMPTION'])

# Predict
if st.button("Predict"):
    st.success("The data is submitted")
    st.balloons()
    st.write("Input DataFrame:")
    st.write(df)
    result = model.predict(df)
    st.write("The predicted carbon emission of your vehicle is:", round(float(result[0]), 2))