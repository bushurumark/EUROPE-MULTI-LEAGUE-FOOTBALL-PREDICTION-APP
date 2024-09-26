#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Define function to preprocess input data
def preprocess_input(HomeTeam, AwayTeam,FTHG,FTAG,HTHG,HTAG,HTR,HS,
                     AS,HST,AST,HF,AF,HC,AC,HY,AY,HR,AR,B365H,B365D,B365A):
    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'HomeTeam': [HomeTeam],
        'AwayTeam': [AwayTeam],
        'FTHG': [FTHG],  
        'FTAG': [FTAG],
        'HTHG': [HTHG],
        'HTAG': [HTAG],
        'HTR': [HTR],
        'HS': [HS],
        'AS': [AS],
        'HST': [HST],
        'AST': [AST],
        'HF': [HF],
        'AF': [AF],
        'HC': [HC],
        'AC': [AC],
        'HY': [HY],
        'AY': [AY],
        'HR': [HR],
        'AR': [AR],
        'B365H': [B365H],
        'B365D': [B365D],
        'B365A': [B365A]
    })
    
    # Encoding of all categorical variables 
    input_data_encoded = pd.get_dummies(input_data)
    
    # Ensure the input data matches the model's expected features
    model_features = model.feature_names_in_
    for feature in model_features:
        if feature not in input_data_encoded.columns:
            input_data_encoded[feature] = 0  # Add missing features with default value 0

    input_data_encoded = input_data_encoded[model_features]

    return input_data_encoded

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: purple;
    }
    .title {
        color: green;
        text-align: center;
        font-size: 40px;
    }
    .widget-label {
        color: #ff6347;
        font-weight: bold;
    }
    .prediction-result {
        color: red;
        font-size: 30px;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Create the web interface
def main():
    st.markdown('<div class="title">Space Prediction Model</div>', unsafe_allow_html=True)

    HomeTeam = st.selectbox(
        'Home Team',  
        ['Man United','Ipswich','Arsenal','Everton','Newcastle',"Nott'm Forest",'West Ham','Brentford',
        'Chelsea','Leicester','Brighton','Crystal Palace','Fulham','Man City','Southampton','Tottenham',
        'Aston Villa','Bournemouth','Wolves','Liverpool']
        )
    AwayTeam = st.selectbox(
        'Away Team',  
        ['Man United','Ipswich','Arsenal','Everton','Newcastle',"Nott'm Forest",'West Ham','Brentford',
        'Chelsea','Leicester','Brighton','Crystal Palace','Fulham','Man City','Southampton','Tottenham',
        'Aston Villa','Bournemouth','Wolves','Liverpool']
        )
    FTHG = st.number_input('FULL TIME HOME TEAM SCORE', min_value=0, max_value=15)
    FTAG = st.number_input('FULL TIME AWAY TEAM SCORE', min_value=0, max_value=15)
    HTHG = st.number_input('HALF TIME HOME TEAM SCORE', min_value=0, max_value=15)
    HTAG = st.number_input('HALF TIME AWAY TEAM SCORE', min_value=0, max_value=15)
    HTR = st.selectbox('HALF TIME RESULTS (H: Home Win, D: Draw, A: Away Win)', ['H', 'D', 'A'])
    HS = st.number_input('HOME TEAM TOTAL SHOTS', min_value=0, max_value=35)
    AS = st.number_input('AWAY TEAM TOTAL SHOTS', min_value=0, max_value=35)
    HST = st.number_input('HOME TEAM SHOTS ON TARGET', min_value=0, max_value=35)
    AST = st.number_input('AWAY TEAM SHOTS ON TARGET', min_value=0, max_value=35)
    HF = st.number_input('HOME TEAM FOULS', min_value=0, max_value=35)
    AF = st.number_input('AWAY TEAM FOULS', min_value=0, max_value=35)
    HC = st.number_input('HOME TEAM CORNERS', min_value=0, max_value=35)
    AC = st.number_input('AWAY TEAM CORNERS', min_value=0, max_value=35)
    HY = st.number_input('HOME TEAM YELLOW CARDS', min_value=0, max_value=25)
    AY = st.number_input('AWAY TEAM YELLOW CARDS', min_value=0, max_value=25)
    HR = st.number_input('HOME TEAM RED CARDS', min_value=0, max_value=25)
    AR = st.number_input('AWAY TEAM RED CARDS', min_value=0, max_value=25)
    B365H = st.number_input('HOME TEAM BETTING ODDS', min_value=0, max_value=40)
    B365D = st.number_input('DRAW BETTING ODDS', min_value=0, max_value=40)
    B365A = st.number_input('HOME TEAM BETTING ODDS', min_value=0, max_value=40)

    if st.button('Predict'):
        input_data = preprocess_input(HomeTeam, AwayTeam,FTHG,FTAG,HTHG,HTAG,HTR,HS,
                                      AS,HST,AST,HF,AF,HC,AC,HY,AY,HR,AR,B365H,B365D,B365A)
        try:
            prediction = model.predict(input_data)[0]
            if 0.5 <= prediction <= 1.4:
                st.markdown('<div class="prediction-result">Prediction: Home Team Win</div>', unsafe_allow_html=True)
            elif 1.5 <= prediction <= 2.4:
                st.markdown('<div class="prediction-result">Prediction: Draw</div>', unsafe_allow_html=True)
            elif 2.5 <= prediction <= 3.4:
                st.markdown('<div class="prediction-result">Prediction: Away Team Win</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="prediction-result">Prediction: Invalid prediction value</div>', unsafe_allow_html=True)
        except Exception as e:
            st.write(f"An error occurred: {e}")
            
if __name__ == '__main__':
    main()



# In[ ]:




