# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Rdepxh4wtVMwXqF3UFV7KCgDPFibqWpk
"""

#!pip install streamlit
# main.py
# main.py
import streamlit as st
from data_loader import download_models, load_data
from controller import run_prediction
from views import (
    render_model_confidence,
    render_historical_probabilities,
    render_recent_form,
    render_head_to_head_history
)
from leagues import leagues
from helpers import initialize_app, get_user_input, initialize_session

# App setup
initialize_app()
initialize_session()

# Load models and data
model1, model2 = download_models()
data1, data2 = load_data()

# User inputs
category, league, home_team, away_team = get_user_input(leagues)

# Prediction logic
if st.button("🔮 Predict Match Outcome"):
    version = "v2" if category == "Others" else "v1"
    data = data2 if version == "v2" else data1
    model = model2 if version == "v2" else model1

    final, full_conf, probs, home_form, away_form, h2h = run_prediction(
        home_team, away_team, model, data, version
    )

    if final is None:
        st.warning("⚠️ Not enough historical data available for prediction.")
        st.session_state.prediction_made = False
    else:
        st.session_state.prediction_made = True
        st.session_state.final = final
        st.session_state.conf = full_conf
        st.session_state.probs = probs
        st.session_state.home_form = home_form
        st.session_state.away_form = away_form
        st.session_state.h2h = h2h

# Output rendering
if st.session_state.get("prediction_made", False):
    st.markdown(
        f'<div class="prediction-result">🏆 Final Prediction: {st.session_state.final}</div>',
        unsafe_allow_html=True
    )

    selected_view = st.selectbox("📊 View More Match Statistics", [
        "Select an option...",
        "Model Confidence",
        "Historical Probabilities",
        "Recent Team Form",
        "Head-to-Head History"
    ])

    if selected_view == "Model Confidence" and st.session_state.conf is not None:
        render_model_confidence(st.session_state.conf)

    elif selected_view == "Historical Probabilities" and st.session_state.probs is not None:
        render_historical_probabilities(st.session_state.probs)

    elif selected_view == "Recent Team Form":
        render_recent_form(home_team, away_team, st.session_state.home_form, st.session_state.away_form)

    elif selected_view == "Head-to-Head History" and not st.session_state.h2h.empty:
        render_head_to_head_history(st.session_state.h2h, home_team, away_team)

