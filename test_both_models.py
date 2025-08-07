#!/usr/bin/env python3
"""
Test script to verify both models are working
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_both_models():
    """Test both models to ensure they're working"""
    
    print("🔍 Testing both models...")
    
    try:
        # Import required modules
        from data_loader import download_models, load_data
        from controller import run_prediction
        
        # Load models and data
        print("📊 Loading models and data...")
        model1, model2 = download_models()
        data1, data2 = load_data()
        
        print(f"✅ Models loaded: {model1 is not None}, {model2 is not None}")
        print(f"✅ Data loaded: {data1 is not None}, {data2 is not None}")
        print(f"📊 Data shapes: {data1.shape if data1 is not None else 'None'}, {data2.shape if data2 is not None else 'None'}")
        
        # Test Model 1 (European leagues)
        print(f"\n🧪 Testing Model 1 (European leagues):")
        home_team = "Groningen"
        away_team = "Feyenoord"
        
        result1 = run_prediction(home_team, away_team, model1, data1, "v1")
        
        if result1:
            prediction1, confidence1, probabilities1, home_form1, away_form1, h2h_data1, has_sufficient_data1, reasons1 = result1
            
            print(f"📊 Model 1 result:")
            print(f"   Prediction: {prediction1}")
            print(f"   Confidence: {confidence1}")
            print(f"   Has sufficient data: {has_sufficient_data1}")
            print(f"   Reasons: {reasons1}")
            
            if probabilities1:
                print(f"📈 Model 1 probability breakdown:")
                for outcome, prob in probabilities1.items():
                    print(f"   {outcome}: {prob:.1%}")
        else:
            print("❌ Model 1 failed")
            
        # Test Model 2 (Other leagues)
        print(f"\n🧪 Testing Model 2 (Other leagues):")
        home_team2 = "Team A"  # Use a team that might be in dataset 2
        away_team2 = "Team B"
        
        result2 = run_prediction(home_team2, away_team2, model2, data2, "v2")
        
        if result2:
            prediction2, confidence2, probabilities2, home_form2, away_form2, h2h_data2, has_sufficient_data2, reasons2 = result2
            
            print(f"📊 Model 2 result:")
            print(f"   Prediction: {prediction2}")
            print(f"   Confidence: {confidence2}")
            print(f"   Has sufficient data: {has_sufficient_data2}")
            print(f"   Reasons: {reasons2}")
            
            if probabilities2:
                print(f"📈 Model 2 probability breakdown:")
                for outcome, prob in probabilities2.items():
                    print(f"   {outcome}: {prob:.1%}")
        else:
            print("❌ Model 2 failed")
            
        # Test team stats API
        print(f"\n🧪 Testing team stats API:")
        import requests
        
        try:
            response = requests.get("http://127.0.0.1:8000/api/team-stats/?team=Man%20United")
            print(f"📊 Team stats API status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Team stats API working: {data.get('team_name', 'Unknown')}")
            else:
                print(f"❌ Team stats API error: {response.text}")
        except Exception as e:
            print(f"❌ Team stats API error: {e}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_both_models() 