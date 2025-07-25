# -*- coding: utf-8 -*-
"""analytics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LZGAb1QqmFbxPOvr0RgntQ7s8bG1G1UQ
"""

import pandas as pd

def get_column_names(version):
    return ("Home", "Away", "Res") if version == "v2" else ("HomeTeam", "AwayTeam", "FTR")

def calculate_probabilities(home, away, data, version="v1"):
    home_col, away_col, result_col = get_column_names(version)
    h2h = data[(data[home_col] == home) & (data[away_col] == away)]
    if h2h.empty:
        return None
    total = len(h2h)
    return {
        "Home Team Win": (h2h[result_col] == 'H').sum() / total * 100,
        "Draw": (h2h[result_col] == 'D').sum() / total * 100,
        "Away Team Win": (h2h[result_col] == 'A').sum() / total * 100,
    }

def get_head_to_head_history(home, away, data, version="v1"):
    home_col, away_col, result_col = get_column_names(version)
    h2h = data[(data[home_col] == home) & (data[away_col] == away)]
    if 'Date' in h2h.columns:
        h2h['Date'] = pd.to_datetime(h2h['Date'], errors='coerce')
    return h2h[['Date', result_col]].dropna()

def get_recent_team_form(home, away, data, version="v1"):
    home_col, away_col, result_col = get_column_names(version)
    home_matches = data[data[home_col] == home].sort_values(by='Date', ascending=False).head(5)
    away_matches = data[data[away_col] == away].sort_values(by='Date', ascending=False).head(5)
    home_form = "".join(home_matches[result_col].fillna("-").values)
    away_form = "".join(away_matches[result_col].fillna("-").values)
    return home_form, away_form

def get_head_to_head_form(home_team, away_team, data, version="v1"):
    home_col, away_col, result_col = get_column_names(version)
    df = data[[home_col, away_col, result_col, "Date"]].copy()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    h2h = df[((df[home_col] == home_team) & (df[away_col] == away_team)) |
             ((df[home_col] == away_team) & (df[away_col] == home_team))].sort_values("Date", ascending=False).head(5)

    home_form, away_form = [], []
    for _, row in h2h.iterrows():
        result = row[result_col]
        h, a = row[home_col], row[away_col]
        home_form.append("W" if ((home_team == h and result == "H") or (home_team == a and result == "A"))
                         else "D" if result == "D" else "L")
        away_form.append("W" if ((away_team == h and result == "H") or (away_team == a and result == "A"))
                         else "D" if result == "D" else "L")
    return "".join(home_form), "".join(away_form)

def get_team_recent_form(team_name, data, version="v1"):
    home_col, away_col, result_col = get_column_names(version)
    df = data[[home_col, away_col, result_col, "Date"]].copy()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    recent_matches = df[(df[home_col] == team_name) | (df[away_col] == team_name)]
    recent_matches = recent_matches.sort_values("Date", ascending=False).head(5)

    form = []
    for _, row in recent_matches.iterrows():
        result = row[result_col]
        is_home = row[home_col] == team_name
        if result == "D":
            form.append("D")
        elif (result == "H" and is_home) or (result == "A" and not is_home):
            form.append("W")
        else:
            form.append("L")
    return "".join(form)