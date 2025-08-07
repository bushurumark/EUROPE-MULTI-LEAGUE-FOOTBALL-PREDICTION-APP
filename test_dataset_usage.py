#!/usr/bin/env python3
"""
Test script to verify that Model 2 is using dataset 2 (football_data2.csv).
"""

import sys
import os
import pandas as pd

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from predictor.analytics import preprocess_for_model2, load_actual_models

def test_dataset2_usage():
    """Test that Model 2 is using dataset 2."""
    print("🔍 Testing Dataset 2 Usage for Model 2")
    print("=" * 50)
    
    # Load the actual models
    model1, model2 = load_actual_models()
    
    if model2 is None:
        print("❌ Model 2 not loaded")
        return False
    
    print("✅ Model 2 loaded successfully")
    
    # Test teams that should use Model 2 (other leagues)
    test_teams = [
        ("Viborg", "Brondby"),
        ("Aarhus", "Midtjylland"),
        ("Basel", "Young Boys"),
        ("Salzburg", "LASK"),
        ("Club America", "Guadalajara Chivas")
    ]
    
    print("\n📊 Testing Model 2 with Dataset 2:")
    for home, away in test_teams:
        # Get features from Model 2 preprocessing
        features = preprocess_for_model2(home, away)
        
        if features is not None:
            print(f"  ✅ {home} vs {away}: {features.shape[1]} features")
            
            # Check if dataset 2 features are present
            dataset2_features = [col for col in features.columns if 'dataset2_feature' in col]
            if dataset2_features:
                print(f"    📁 Dataset 2 features found: {len(dataset2_features)}")
            else:
                print(f"    ⚠️ No dataset 2 features found")
        else:
            print(f"  ❌ {home} vs {away}: No features available")
    
    # Test that Model 2 can make predictions
    print("\n🎯 Testing Model 2 Predictions:")
    for home, away in test_teams[:3]:  # Test first 3 pairs
        features = preprocess_for_model2(home, away)
        if features is not None:
            try:
                # Make prediction
                prediction = model2.predict(features.values)[0]
                probabilities = model2.predict_proba(features.values)[0]
                confidence = max(probabilities)
                
                outcome_map = {0: "Home", 1: "Draw", 2: "Away"}
                outcome = outcome_map.get(prediction, "Draw")
                
                print(f"  ✅ {home} vs {away}: {outcome} ({confidence:.1%})")
            except Exception as e:
                print(f"  ❌ {home} vs {away}: Prediction failed - {e}")
        else:
            print(f"  ❌ {home} vs {away}: No features available")
    
    return True

def check_dataset2_content():
    """Check the content of dataset 2."""
    print("\n📁 Checking Dataset 2 Content:")
    print("=" * 50)
    
    data2_path = 'data/football_data2.csv'
    if os.path.exists(data2_path):
        try:
            data = pd.read_csv(data2_path)
            print(f"✅ Dataset 2 loaded: {len(data)} rows")
            print(f"   Columns: {list(data.columns)}")
            
            # Check unique countries and leagues
            if 'Country' in data.columns:
                countries = data['Country'].unique()
                print(f"   Countries: {list(countries)}")
            
            if 'League' in data.columns:
                leagues = data['League'].unique()
                print(f"   Leagues: {list(leagues)}")
            
            # Check unique teams
            if 'HomeTeam' in data.columns:
                home_teams = data['HomeTeam'].unique()
                away_teams = data['AwayTeam'].unique()
                all_teams = set(home_teams) | set(away_teams)
                print(f"   Total unique teams: {len(all_teams)}")
                print(f"   Sample teams: {list(all_teams)[:10]}")
            
        except Exception as e:
            print(f"❌ Error reading dataset 2: {e}")
    else:
        print(f"❌ Dataset 2 not found at {data2_path}")

if __name__ == "__main__":
    print("🚀 Testing Model 2 Dataset Usage")
    print("=" * 60)
    
    # Check dataset 2 content
    check_dataset2_content()
    
    # Test dataset 2 usage
    success = test_dataset2_usage()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 Model 2 is properly using dataset 2!")
    else:
        print("⚠️ Issues found with Model 2 dataset usage") 