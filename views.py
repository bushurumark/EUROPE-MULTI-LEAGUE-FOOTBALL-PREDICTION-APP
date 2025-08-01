# -*- coding: utf-8 -*-
"""views.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w3luDBZ-0-wEnJvGrYQIjJqZCjNUoSUy
"""

import streamlit as st
import plotly.express as px
import pandas as pd

def render_model_confidence(conf_dict):
    st.subheader("🤖 Model Confidence")
    # Convert to DataFrame
    df = pd.DataFrame({
        "Outcome": list(conf_dict.keys()),
        "Confidence (%)": [v * 100 for v in conf_dict.values()]
    })
    fig = px.bar(
        df,
        x="Outcome",
        y="Confidence (%)",
        title="Model Output Probabilities",
        color="Outcome",
        color_discrete_map={
            "Home Win": "green",
            "Draw": "yellow",
            "Away Win": "red"
        }
    )
    st.plotly_chart(fig)
    for outcome, prob in conf_dict.items():
        st.markdown(f"**{outcome}**: {prob * 100:.2f}%")

def render_historical_probabilities(probs):
    st.subheader("📚 Historical Probabilities")
    df = pd.DataFrame({
        "Outcome": list(probs.keys()),
        "Probability (%)": [v for v in probs.values()]
    })
    fig = px.bar(
        df,
        x="Outcome",
        y="Probability (%)",
        title="Historical Match Outcome Probabilities",
        color="Outcome",
        color_discrete_map={
            "Home Team Win": "green",
            "Draw": "yellow",
            "Away Team Win": "red"
        }
    )
    st.plotly_chart(fig)
    for outcome, pct in probs.items():
        st.markdown(f"**{outcome}**: {pct:.2f}%")

def render_recent_form(home_team, away_team, home_form, away_form):
    st.subheader("📈 Recent Team Form (Last 5 Matches)")
    st.markdown(f"**{home_team}**: `{home_form}`")
    st.markdown(f"**{away_team}**: `{away_form}`")

def render_head_to_head_history(h2h, home_team, away_team):
    st.subheader("🔁 Head-to-Head Results")
    df = h2h.copy()
    result_col = 'FTR' if 'FTR' in df.columns else 'Res'
    result_map = {'H': 'Home Win', 'D': 'Draw', 'A': 'Away Win'}
    df['Result'] = df[result_col].map(result_map)
    fig = px.histogram(
        df, x='Date', color='Result',
        title=f"{home_team} vs {away_team} - Head-to-Head",
        color_discrete_map={
            "Home Win": "green", 
            "Draw": "yellow", 
            "Away Win": "red"
        }
    )
    st.plotly_chart(fig)
    st.dataframe(df[['Date', 'Result']].sort_values(by='Date', ascending=False).reset_index(drop=True))
