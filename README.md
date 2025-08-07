# Football Prediction App - Core Logic

A cleaned version containing only the essential logic parts for football match prediction.

## Core Files

### Main Application
- `main_terminal.py` - Terminal-based prediction app
- `requirements_terminal.txt` - Dependencies for terminal version

### Core Logic
- `analytics.py` - Analytics and data processing functions
- `controller.py` - Prediction controller logic
- `data_loader.py` - Data loading utilities
- `model_utils.py` - Model utility functions
- `constants.py` - Application constants
- `leagues.py` - League and team data

### Data & Models
- `Models/` - Trained machine learning models
- `Datasets/` - Football datasets

## Quick Start

```bash
# Install dependencies
pip install -r requirements_terminal.txt

# Run the app
python main_terminal.py
```

## Features

- 🎯 Match outcome prediction
- 📊 Model confidence analysis
- 📈 Team form analysis
- 🔄 Head-to-head statistics
- 🏆 Multiple European leagues support

## Project Structure

```
EUROPE-MULTI-LEAGUE-FOOTBALL-PREDICTION-APP/
├── main_terminal.py          # Main terminal application
├── requirements_terminal.txt  # Dependencies
├── analytics.py              # Analytics logic
├── controller.py             # Prediction controller
├── data_loader.py            # Data loading
├── model_utils.py            # Model utilities
├── constants.py              # App constants
├── leagues.py                # League data
├── Models/                   # Trained models
│   ├── model1.pkl
│   └── model2.pkl
└── Datasets/                 # Football datasets
    ├── football_data1.csv
    └── football_data2.csv
```

## Removed Files

The following unnecessary files were removed:
- ❌ `main.py` (Streamlit web version)
- ❌ `views.py` (Streamlit views)
- ❌ `helpers.py` (Streamlit helpers)
- ❌ `style.css` (web styling)
- ❌ `render.yaml` (deployment config)
- ❌ `requirements.txt` (web requirements)
- ❌ `ML_TRAINING.ipynb` (large training notebook)
- ❌ `README_TERMINAL.md` (old documentation)
- ❌ `__pycache__/` (Python cache)

## Usage

1. Select a football category
2. Choose a league
3. Pick home and away teams
4. Get prediction results

The app provides:
- Final match prediction
- Model confidence percentages
- Historical probabilities
- Recent team form
- Head-to-head history 