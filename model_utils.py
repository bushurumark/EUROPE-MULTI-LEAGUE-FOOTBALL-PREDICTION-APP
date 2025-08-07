# -*- coding: utf-8 -*-
"""Model utilities for football prediction app.

This module provides utility functions for:
- Feature alignment with trained models
- Team statistics computation
- Probability calculations
- Prediction confidence scoring
- Final prediction determination
"""

import pandas as pd
import numpy as np
import logging
from typing import Optional, Dict, Tuple, Any
from analytics import get_column_names

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def align_features(input_df: pd.DataFrame, model) -> pd.DataFrame:
    """Align input DataFrame features with model's expected features.
    
    Args:
        input_df: Input DataFrame with features
        model: Trained model with feature_names_in_ attribute
        
    Returns:
        DataFrame with aligned features matching model's expected input
    """
    # Create a copy to avoid fragmentation
    aligned_df = input_df.copy()
    
    # Get missing features
    missing_features = [f for f in model.feature_names_in_ if f not in aligned_df.columns]
    
    if missing_features:
        logger.info(f"Adding {len(missing_features)} missing features with default values")
        # Create missing features DataFrame
        missing_df = pd.DataFrame({feature: 0 for feature in missing_features}, index=aligned_df.index)
        # Use concat to avoid fragmentation
        aligned_df = pd.concat([aligned_df, missing_df], axis=1)
    
    # Ensure correct column order
    return aligned_df[model.feature_names_in_]

def compute_mean_for_teams(home: str, away: str, data: pd.DataFrame, model, version: str = "v1") -> pd.DataFrame:
    """Compute mean statistics for head-to-head matches between teams.
    
    Args:
        home: Home team name
        away: Away team name
        data: Historical match data
        model: Trained model for feature alignment
        version: Data version ("v1" or "v2")
        
    Returns:
        DataFrame with mean statistics aligned to model features, or fallback statistics if no data
        
    Raises:
        ValueError: If invalid version or missing required columns
    """
    if version not in ["v1", "v2"]:
        raise ValueError("Version must be 'v1' or 'v2'")
    
    home_col, away_col, result_col = get_column_names(version)
    
    # Team name variations for better matching
    team_variations = {
        'man city': 'Man City',
        'manchester city': 'Man City',
        'man united': 'Man United', 
        'manchester united': 'Man United',
        'newcastle': 'Newcastle',
        'newcastle united': 'Newcastle',
        'west ham': 'West Ham',
        'west ham united': 'West Ham',
        'brighton': 'Brighton',
        'brighton & hove albion': 'Brighton',
        'leicester': 'Leicester',
        'leicester city': 'Leicester',
        'wolves': 'Wolves',
        'wolverhampton wanderers': 'Wolves',
        'nottingham forest': "Nott'm Forest",
        'nottingham': "Nott'm Forest",
        'ipswich': 'Ipswich',
        'ipswich town': 'Ipswich',
        'leeds': 'Leeds',
        'leeds united': 'Leeds',
        'luton': 'Luton',
        'luton town': 'Luton',
        'sheffield wednesday': 'Sheffield Weds',
        'coventry': 'Coventry',
        'coventry city': 'Coventry',
        'plymouth': 'Plymouth',
        'plymouth argyle': 'Plymouth',
        'stoke': 'Stoke',
        'stoke city': 'Stoke',
        'west brom': 'West Brom',
        'west bromwich albion': 'West Brom',
        'qpr': 'QPR',
        'queens park rangers': 'QPR',
        'norwich': 'Norwich',
        'norwich city': 'Norwich',
        'oxford': 'Oxford',
        'oxford united': 'Oxford',
        'swansea': 'Swansea',
        'swansea city': 'Swansea',
        'cardiff': 'Cardiff',
        'cardiff city': 'Cardiff',
        'hull': 'Hull',
        'hull city': 'Hull',
        'blackburn': 'Blackburn',
        'blackburn rovers': 'Blackburn',
        'derby': 'Derby',
        'derby county': 'Derby',
        'preston': 'Preston',
        'preston north end': 'Preston',
        # Russian teams
        'krasnodar': 'Krasnodar',
        'akron togliatti': 'Akron Togliatti',
        'zenit': 'Zenit',
        'zenit st petersburg': 'Zenit',
        'dynamo moscow': 'Dynamo Moscow',
        'dynamo': 'Dynamo Moscow',
        'cska moscow': 'CSKA Moscow',
        'cska': 'CSKA Moscow',
        'spartak moscow': 'Spartak Moscow',
        'spartak': 'Spartak Moscow',
        'lokomotiv moscow': 'Lokomotiv Moscow',
        'lokomotiv': 'Lokomotiv Moscow',
        'rubin kazan': 'Rubin Kazan',
        'rubin': 'Rubin Kazan',
        'rostov': 'FK Rostov',
        'fk rostov': 'FK Rostov',
        'orenburg': 'Orenburg',
        'akhmat grozny': 'Akhmat Grozny',
        'akhmat': 'Akhmat Grozny',
        'krasnodar': 'Krasnodar',
        'krasnodar fc': 'Krasnodar',
        'fakel voronezh': 'Fakel Voronezh',
        'fakel': 'Fakel Voronezh',
        'krylya sovetov': 'Krylya Sovetov',
        'krylya': 'Krylya Sovetov',
        'khimki': 'Khimki',
        'dynamo makhachkala': 'Dynamo Makhachkala',
        'pari nn': 'Pari NN',
        'pari': 'Pari NN',
        # Swiss teams
        'young boys': 'Young Boys',
        'young boys bern': 'Young Boys',
        'yverdon': 'Yverdon',
        'yverdon sport': 'Yverdon',
        'basel': 'Basel',
        'fc basel': 'Basel',
        'grasshoppers': 'Grasshoppers',
        'grasshoppers zurich': 'Grasshoppers',
        'lausanne': 'Lausanne',
        'lausanne sport': 'Lausanne',
        'lugano': 'Lugano',
        'fc lugano': 'Lugano',
        'luzern': 'Luzern',
        'fc luzern': 'Luzern',
        'servette': 'Servette',
        'servette geneva': 'Servette',
        'sion': 'Sion',
        'fc sion': 'Sion',
        'st. gallen': 'St. Gallen',
        'st gallen': 'St. Gallen',
        'winterthur': 'Winterthur',
        'fc winterthur': 'Winterthur',
        'zurich': 'Zurich',
        'fc zurich': 'Zurich',
    }
    
    # Try to find the correct team names
    home_search = home.lower()
    away_search = away.lower()
    
    if home_search in team_variations:
        home = team_variations[home_search]
    if away_search in team_variations:
        away = team_variations[away_search]
    
    # Validate required columns exist
    required_cols = [home_col, away_col, result_col]
    missing_cols = [col for col in required_cols if col not in data.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    # Filter head-to-head matches
    h2h = data[(data[home_col] == home) & (data[away_col] == away)]
    
    if h2h.empty:
        logger.warning(f"No head-to-head data found for {home} vs {away}. Using fallback statistics.")
        # Create fallback statistics based on league averages
        return create_fallback_statistics(model, version)
    
    # Remove non-numeric columns for mean calculation
    exclude_cols = [result_col, "Date", "Country", "League", "Season", "Time"]
    h2h = h2h.drop(columns=[col for col in exclude_cols if col in h2h.columns], errors='ignore')
    
    # Handle HTR column conversion for v1
    if version == "v1" and 'HTR' in h2h.columns:
        h2h['HTR'] = h2h['HTR'].replace({'H': 1, 'D': 2, 'A': 3})
    
    # Calculate mean statistics
    mean = h2h.mean(numeric_only=True)
    
    # Convert HTR back to categorical if present
    if 'HTR' in mean:
        htr_value = mean['HTR']
        if 0 <= htr_value <= 1.4:
            mean['HTR'] = 'H'
        elif 1.5 <= htr_value <= 2.4:
            mean['HTR'] = 'D'
        else:
            mean['HTR'] = 'A'
    
    # Create DataFrame with single row
    result_df = pd.DataFrame([mean])
    
    # Align features with model
    return align_features(result_df, model)


def create_fallback_statistics(model, version: str = "v1") -> pd.DataFrame:
    """Create fallback statistics when teams are not found in dataset.
    
    Args:
        model: Trained model for feature alignment
        version: Data version
        
    Returns:
        DataFrame with default statistics aligned to model features
    """
    # Default statistics based on typical football match data
    default_stats = {
        'HomeTeam': 1.0,
        'AwayTeam': 1.0,
        'FTHG': 1.5,  # Average home goals
        'FTAG': 1.2,  # Average away goals
        'HTHG': 0.8,  # Average home half-time goals
        'HTAG': 0.6,  # Average away half-time goals
        'HS': 12.0,   # Average home shots
        'AS': 10.0,   # Average away shots
        'HST': 4.5,   # Average home shots on target
        'AST': 3.8,   # Average away shots on target
        'HC': 5.0,    # Average home corners
        'AC': 4.5,    # Average away corners
        'HF': 12.0,   # Average home fouls
        'AF': 11.0,   # Average away fouls
        'HY': 1.5,    # Average home yellow cards
        'AY': 1.4,    # Average away yellow cards
        'HR': 0.1,    # Average home red cards
        'AR': 0.1,    # Average away red cards
        'HTR': 'D',   # Default half-time result (Draw)
        'FTR': 'D',   # Default full-time result (Draw)
    }
    
    # Add version-specific defaults
    if version == "v1":
        default_stats.update({
            'BbMxH': 2.1,  # Max home odds
            'BbAvH': 2.0,  # Average home odds
            'BbMxD': 3.2,  # Max draw odds
            'BbAvD': 3.1,  # Average draw odds
            'BbMxA': 3.8,  # Max away odds
            'BbAvA': 3.7,  # Average away odds
        })
    
    # Create DataFrame with single row
    result_df = pd.DataFrame([default_stats])
    
    # Align features with model
    return align_features(result_df, model)

def calculate_probabilities(home: str, away: str, data: pd.DataFrame, version: str = "v1") -> Optional[Dict[str, float]]:
    """Calculate win/draw/loss probabilities based on historical head-to-head data.
    
    Args:
        home: Home team name
        away: Away team name
        data: Historical match data
        version: Data version ("v1" or "v2")
        
    Returns:
        Dictionary with probabilities for each outcome, or None if no data
    """
    home_col, away_col, result_col = get_column_names(version)
    outcome_map = {"H": "Home Team Win", "D": "Draw", "A": "Away Team Win"}
    
    # Team name variations for better matching
    team_variations = {
        'man city': 'Man City',
        'manchester city': 'Man City',
        'man united': 'Man United', 
        'manchester united': 'Man United',
        'newcastle': 'Newcastle',
        'newcastle united': 'Newcastle',
        'west ham': 'West Ham',
        'west ham united': 'West Ham',
        'brighton': 'Brighton',
        'brighton & hove albion': 'Brighton',
        'leicester': 'Leicester',
        'leicester city': 'Leicester',
        'wolves': 'Wolves',
        'wolverhampton wanderers': 'Wolves',
        'nottingham forest': "Nott'm Forest",
        'nottingham': "Nott'm Forest",
        'ipswich': 'Ipswich',
        'ipswich town': 'Ipswich',
        'leeds': 'Leeds',
        'leeds united': 'Leeds',
        'luton': 'Luton',
        'luton town': 'Luton',
        'sheffield wednesday': 'Sheffield Weds',
        'coventry': 'Coventry',
        'coventry city': 'Coventry',
        'plymouth': 'Plymouth',
        'plymouth argyle': 'Plymouth',
        'stoke': 'Stoke',
        'stoke city': 'Stoke',
        'west brom': 'West Brom',
        'west bromwich albion': 'West Brom',
        'qpr': 'QPR',
        'queens park rangers': 'QPR',
        'norwich': 'Norwich',
        'norwich city': 'Norwich',
        'oxford': 'Oxford',
        'oxford united': 'Oxford',
        'swansea': 'Swansea',
        'swansea city': 'Swansea',
        'cardiff': 'Cardiff',
        'cardiff city': 'Cardiff',
        'hull': 'Hull',
        'hull city': 'Hull',
        'blackburn': 'Blackburn',
        'blackburn rovers': 'Blackburn',
        'derby': 'Derby',
        'derby county': 'Derby',
        'preston': 'Preston',
        'preston north end': 'Preston',
        # Russian teams
        'krasnodar': 'Krasnodar',
        'akron togliatti': 'Akron Togliatti',
        'zenit': 'Zenit',
        'zenit st petersburg': 'Zenit',
        'dynamo moscow': 'Dynamo Moscow',
        'dynamo': 'Dynamo Moscow',
        'cska moscow': 'CSKA Moscow',
        'cska': 'CSKA Moscow',
        'spartak moscow': 'Spartak Moscow',
        'spartak': 'Spartak Moscow',
        'lokomotiv moscow': 'Lokomotiv Moscow',
        'lokomotiv': 'Lokomotiv Moscow',
        'rubin kazan': 'Rubin Kazan',
        'rubin': 'Rubin Kazan',
        'rostov': 'FK Rostov',
        'fk rostov': 'FK Rostov',
        'orenburg': 'Orenburg',
        'akhmat grozny': 'Akhmat Grozny',
        'akhmat': 'Akhmat Grozny',
        'krasnodar': 'Krasnodar',
        'krasnodar fc': 'Krasnodar',
        'fakel voronezh': 'Fakel Voronezh',
        'fakel': 'Fakel Voronezh',
        'krylya sovetov': 'Krylya Sovetov',
        'krylya': 'Krylya Sovetov',
        'khimki': 'Khimki',
        'dynamo makhachkala': 'Dynamo Makhachkala',
        'pari nn': 'Pari NN',
        'pari': 'Pari NN',
        # Swiss teams
        'young boys': 'Young Boys',
        'young boys bern': 'Young Boys',
        'yverdon': 'Yverdon',
        'yverdon sport': 'Yverdon',
        'basel': 'Basel',
        'fc basel': 'Basel',
        'grasshoppers': 'Grasshoppers',
        'grasshoppers zurich': 'Grasshoppers',
        'lausanne': 'Lausanne',
        'lausanne sport': 'Lausanne',
        'lugano': 'Lugano',
        'fc lugano': 'Lugano',
        'luzern': 'Luzern',
        'fc luzern': 'Luzern',
        'servette': 'Servette',
        'servette geneva': 'Servette',
        'sion': 'Sion',
        'fc sion': 'Sion',
        'st. gallen': 'St. Gallen',
        'st gallen': 'St. Gallen',
        'winterthur': 'Winterthur',
        'fc winterthur': 'Winterthur',
        'zurich': 'Zurich',
        'fc zurich': 'Zurich',
    }
    
    # Try to find the correct team names
    home_search = home.lower()
    away_search = away.lower()
    
    if home_search in team_variations:
        home = team_variations[home_search]
    if away_search in team_variations:
        away = team_variations[away_search]
    
    h2h = data[(data[home_col] == home) & (data[away_col] == away)]
    
    if h2h.empty:
        logger.warning(f"No head-to-head data found for {home} vs {away}")
        return None
    
    # Calculate probabilities
    value_counts = h2h[result_col].value_counts(normalize=True) * 100
    
    # Ensure all outcomes are present with 0% if missing
    for outcome in ['H', 'D', 'A']:
        if outcome not in value_counts:
            value_counts[outcome] = 0.0
    
    return {outcome_map.get(k, k): round(v, 2) for k, v in value_counts.items()}

def predict_with_confidence(model, input_df: pd.DataFrame) -> Tuple[Optional[str], Optional[float], Optional[Dict[str, float]]]:
    """Make prediction with confidence scores using trained model.
    
    Args:
        model: Trained classification model
        input_df: Input features DataFrame
        
    Returns:
        Tuple of (predicted_label, confidence_score, all_probabilities)
    """
    try:
        # Get prediction probabilities
        proba = model.predict_proba(input_df)[0]
        pred_idx = proba.argmax()
        labels = model.classes_
        
        # The models predict numeric values: 1=Home Win, 2=Draw, 3=Away Win
        predicted_numeric = labels[pred_idx]
        confidence_score = proba[pred_idx]
        
        # Convert numeric prediction to string label
        pred_map = {1: "Home Team Win", 2: "Draw", 3: "Away Team Win"}
        predicted_label = pred_map.get(predicted_numeric, "Draw")
        
        # Create probability dictionary with string labels
        all_probabilities = {
            "Home Team Win": proba[0] if len(proba) > 0 else 0.0,
            "Draw": proba[1] if len(proba) > 1 else 0.0,
            "Away Team Win": proba[2] if len(proba) > 2 else 0.0
        }
        
        logger.info(f"Prediction: {predicted_label} (numeric: {predicted_numeric}) with confidence: {confidence_score:.3f}")
        
        return predicted_label, confidence_score, all_probabilities
        
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return None, None, None

def determine_final_prediction(pred: float, probs: Dict[str, float]) -> str:
    """Determine final prediction based on model output and historical probabilities.
    
    Args:
        pred: Model prediction value (0-3.4 scale)
        probs: Historical probability dictionary
        
    Returns:
        Final prediction string with reasoning - can include multiple outcomes
    """
    # Debug logging
    logger.info(f"determine_final_prediction called with pred={pred}, probs={probs}")
    
    # Map prediction ranges to outcomes
    if 0 <= pred <= 1.4:
        model_outcome = "Home Team Win"
    elif 1.5 <= pred <= 2.4:
        model_outcome = "Draw"
    elif 2.5 <= pred <= 3.4:
        model_outcome = "Away Team Win"
    else:
        logger.warning(f"Invalid prediction value: {pred}")
        return "❗ Invalid prediction"
    
    logger.info(f"Model outcome: {model_outcome}")
    
    # If no historical probabilities, return model outcome
    if not probs:
        logger.info("No historical probabilities, returning model outcome")
        return model_outcome
    
    # Find highest historical probability
    highest = max(probs, key=probs.get)
    highest_prob = probs[highest]
    
    logger.info(f"Highest historical probability: {highest} ({highest_prob})")
    
    # Check for close probabilities (within 10% of each other)
    close_outcomes = []
    for outcome, prob in probs.items():
        if abs(prob - highest_prob) <= 0.1:  # Within 10% of highest
            close_outcomes.append(outcome)
    
    logger.info(f"Close outcomes: {close_outcomes}")
    
    # If model and historical agree, return single prediction
    if model_outcome == highest:
        logger.info("Model and historical agree, returning single prediction")
        return model_outcome
    
    # If there are multiple close outcomes, show uncertainty
    if len(close_outcomes) >= 2:
        if model_outcome in close_outcomes:
            # Model agrees with one of the close outcomes
            other_close = [o for o in close_outcomes if o != model_outcome]
            if other_close:
                result = f"{model_outcome} or {other_close[0]}"
                logger.info(f"Multiple close outcomes with model agreement: {result}")
                return result
            else:
                result = f"{close_outcomes[0]} or {close_outcomes[1]}"
                logger.info(f"Multiple close outcomes: {result}")
                return result
        else:
            # Model disagrees with close outcomes
            result = f"{model_outcome} or {close_outcomes[0]}"
            logger.info(f"Model disagrees with close outcomes: {result}")
            return result
    
    # Single disagreement - show both possibilities
    result = f"{model_outcome} or {highest}"
    logger.info(f"Single disagreement: {result}")
    return result

def validate_team_names(home: str, away: str, data: pd.DataFrame, version: str = "v1") -> Tuple[bool, str]:
    """Validate that team names exist in the dataset.
    
    Args:
        home: Home team name
        away: Away team name
        data: Historical match data
        version: Data version
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    home_col, away_col, _ = get_column_names(version)
    
    all_teams = set(data[home_col].unique()) | set(data[away_col].unique())
    
    missing_teams = []
    if home not in all_teams:
        missing_teams.append(home)
    if away not in all_teams:
        missing_teams.append(away)
    
    if missing_teams:
        return False, f"Teams not found in dataset: {', '.join(missing_teams)}"
    
    return True, ""

def get_prediction_summary(home: str, away: str, model, data: pd.DataFrame, version: str = "v1") -> Dict[str, Any]:
    """Generate comprehensive prediction summary for a match.
    
    Args:
        home: Home team name
        away: Away team name
        model: Trained model
        data: Historical match data
        version: Data version
        
    Returns:
        Dictionary containing all prediction information
    """
    # Check if teams exist in dataset
    is_valid, error_msg = validate_team_names(home, away, data, version)
    
    if not is_valid:
        logger.warning(f"Teams not found in dataset: {error_msg}. Using fallback prediction.")
        return create_fallback_prediction(home, away, model, version)
    
    # Get historical probabilities
    hist_probs = calculate_probabilities(home, away, data, version)
    
    # Get model features
    model_features = compute_mean_for_teams(home, away, data, model, version)
    
    # Make prediction
    pred_label, confidence, all_probs = predict_with_confidence(model, model_features)
    
    if pred_label is None:
        return {"error": "Model prediction failed"}
    
    # Convert prediction to numeric for final determination
    pred_map = {"Home Team Win": 1.0, "Draw": 2.0, "Away Team Win": 3.0}
    pred_value = pred_map.get(pred_label, 2.0)
    
    # Determine final prediction
    final_pred = determine_final_prediction(pred_value, hist_probs or {})
    
    return {
        "home_team": home,
        "away_team": away,
        "model_prediction": pred_label,
        "model_confidence": confidence,
        "historical_probabilities": hist_probs,
        "final_prediction": final_pred,
        "all_model_probabilities": all_probs,
        "data_available": True
    }


def create_fallback_prediction(home: str, away: str, model, version: str = "v1") -> Dict[str, Any]:
    """Create fallback prediction when teams are not found in dataset.
    
    Args:
        home: Home team name
        away: Away team name
        model: Trained model
        version: Data version
        
    Returns:
        Dictionary containing fallback prediction information
    """
    # Get fallback statistics
    fallback_features = create_fallback_statistics(model, version)
    
    # Make prediction with fallback data
    pred_label, confidence, all_probs = predict_with_confidence(model, fallback_features)
    
    if pred_label is None:
        # If model prediction fails, use default prediction
        pred_label = "Draw"
        confidence = 0.5
        all_probs = {"Home Team Win": 0.33, "Draw": 0.34, "Away Team Win": 0.33}
    
    # Create fallback historical probabilities
    fallback_hist_probs = {
        "Home Team Win": 0.33,
        "Draw": 0.34,
        "Away Team Win": 0.33
    }
    
    # Convert prediction to numeric for final determination
    pred_map = {"Home Team Win": 1.0, "Draw": 2.0, "Away Team Win": 3.0}
    pred_value = pred_map.get(pred_label, 2.0)
    
    # Determine final prediction
    final_pred = determine_final_prediction(pred_value, fallback_hist_probs)
    
    return {
        "home_team": home,
        "away_team": away,
        "model_prediction": pred_label,
        "model_confidence": confidence,
        "historical_probabilities": fallback_hist_probs,
        "final_prediction": final_pred,
        "all_model_probabilities": all_probs,
        "data_available": False,
        "warning": f"Teams '{home}' and '{away}' not found in dataset. Using fallback prediction based on league averages."
    }

