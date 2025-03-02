import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pickel", "rb"))


st.title("Car price Prediction")


#select Brand 
Brand = st.selectbox("Brand; ", ['Kia', 'Bmw','Chevrolet','Audi','Mercedes','Volkswagen','Hyundai','Ford','Honda',])
Brand_mapping = {'Kia': 0, 'Bmw': 1,'Chevrolet': 2,'Audi': 3,'Mercedes': 4,'Volkswagen': 5,'Hyundai': 6,'Ford': 7,'Honda': 9,}
Brand_value = Brand_mapping.get(Brand)


#select Model
Model = st.selectbox("Model; ",['Rio','Malibu','GLA','q5','Golf','Carmy','Civic','Sportage','RAV4','5 Series','CR-v','Elantra','Tiagun','Explorer','A3','3 Series','Tuscon','Passat','Impala','Corolla','Optima','Fiesta','A4','Focus','E-class','sonata','C-class','X5','Accord'])
Model_mapping = {'Rio': 0,'Malibu': 1,'GLA': 2,'q5': 3,'Golf': 4,'Carmy': 5,'Civic': 6,'Sportage': 7,'RAV4': 8,'5 Series': 9,'CR-v': 10,'Elantra': 11,'Tiagun': 12,'Explorer': 13,'A3': 14,'3 Series': 15,'Tuscon': 16,'Passat': 17,'Impala': 18,'Corolla': 19,'Optima': 20,'Fiesta': 21,'A4': 22,'Focus': 23,'E-class': 24,'sonata': 25,'C-class': 26,'X5': 27,'Accord': 28}
Model_value = Model_mapping.get(Model)


#Year of the car
year =st.text_input("Year",key='1')

#engine size
Eng_Size= st.text_input("engine size",key='2')

#Fuel type

Fuel_Type= st.selectbox("Fuel_Type",['Diesel','petrol','Hybrid',"Electric"])
Fuel_Type_mapping = {'Diesel': 0,'petrol': 1,'Hybrid': 2,"Electric": 3}
Fuel_Type_value = Fuel_Type_mapping.get(Fuel_Type)

#Transmission
Transmission= st.selectbox("Transmission",['Automatic','Manual','Semi-Automatic'])
Transmission_mapping = {'Automatic': 0,'Manual': 1,'Semi-Automatic': 2}
Transmission_value = Transmission_mapping.get(Transmission)

#Mieage
Mileage= st.text_input("Mileage",key='3')

#select doors
Doors= st.selectbox("Doors",['2','3','4','5'])
#Owners
Owners= st.selectbox("Owners",['1','2','3','4','5'])
try:
    year = int(year) if year.isdigit() else 0
except ValueError:
    year = 0

try:
    Eng_Size = float(Eng_Size) if Eng_Size.replace('.', '', 1).isdigit() else 0.0
except ValueError:
    Eng_Size = 0.0

try:
    Mileage = float(Mileage) if Mileage.replace('.', '', 1).isdigit() else 0.0
except ValueError:
    Mileage = 0.0

Brand_value = Brand_mapping.get(Brand)
Model_value = Model_mapping.get(Model)
Fuel_Type_value = Fuel_Type_mapping.get(Fuel_Type)
Transmission_value = Transmission_mapping.get(Transmission)
Doors_value = int(Doors)  # Doors are expected to be an integer
Owners_value = int(Owners)  # Owners are expected to be an integer
if st.button("click"):
    # Assuming Fuel_Type_value and Transmission_value have already been assigned based on the selected values
    inp = np.array([[Brand_value, Model_value, year, Eng_Size, Fuel_Type_value, Transmission_value, Mileage, Doors_value, Owners_value]])


    prediction = model.predict(inp)
    print(prediction)
    st.success(f"Price: ${prediction[0] : .2F}")
    






