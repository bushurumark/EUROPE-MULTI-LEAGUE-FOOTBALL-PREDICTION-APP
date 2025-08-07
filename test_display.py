#!/usr/bin/env python3
"""
Test script to verify prediction probabilities display
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_loader import load_data, download_models
from model_utils import get_prediction_summary

def test_prediction_display():
    """Test that prediction probabilities are displayed correctly"""
    
    print("🔍 Testing Prediction Probabilities Display")
    print("=" * 50)
    
    try:
        # Load data and models
        print("📊 Loading data and models...")
        data1, data2 = load_data()
        model1, model2 = download_models()
        
        # Test with real teams from dataset 2
        test_cases = [
            ("Basel", "Young Boys"),
            ("CFR Cluj", "Astra"),
            ("CSKA Moscow", "Dynamo Moscow")
        ]
        
        print("\n🇪🇺 Testing Prediction Display (Dataset 2)")
        print("-" * 40)
        
        for team1, team2 in test_cases:
            print(f"\n🏆 Testing: {team1} vs {team2}")
            
            # Get prediction summary
            result = get_prediction_summary(team1, team2, model2, data2, version="v2")
            
            if result and 'error' not in result:
                print(f"✅ Prediction successful!")
                print(f"   Final prediction: {result.get('final_prediction', 'Unknown')}")
                print(f"   Model prediction: {result.get('model_prediction', 'Unknown')}")
                print(f"   Model confidence: {result.get('model_confidence', 0):.2f}")
                
                # Check prediction probabilities (showing historical probabilities)
                hist_probs = result.get('historical_probabilities', {})
                if hist_probs:
                    print(f"   🤖 Prediction Probabilities:")
                    for outcome, prob in hist_probs.items():
                        if outcome == "Home Team Win":
                            print(f"     Home Win {prob:.1f}%")
                        elif outcome == "Draw":
                            print(f"     Draw {prob:.1f}%")
                        elif outcome == "Away Team Win":
                            print(f"     Away Win {prob:.1f}%")
                        else:
                            print(f"     {outcome} {prob:.1f}%")
                
                # Check model probabilities (for reference)
                model_probs = result.get('all_model_probabilities', {})
                if model_probs:
                    print(f"   📊 Model Probabilities:")
                    for outcome, prob in model_probs.items():
                        print(f"     • {outcome}: {prob * 100:.2f}%")
                
                print(f"   Data available: {result.get('data_available', False)}")
            else:
                print(f"❌ Prediction failed: {result.get('error', 'Unknown error')}")
        
        print("\n✅ Prediction display test completed!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_prediction_display() 