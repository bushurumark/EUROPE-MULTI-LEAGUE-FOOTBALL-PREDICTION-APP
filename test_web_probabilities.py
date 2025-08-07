#!/usr/bin/env python3
"""
Test to verify that historical probabilities are being passed correctly to the web interface
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_loader import load_data, download_models
from controller import run_prediction

def test_web_probabilities():
    """Test that historical probabilities are correctly formatted for web interface"""
    
    print("🔍 Testing Web Interface Historical Probabilities")
    print("=" * 50)
    
    try:
        # Load data and models
        print("📊 Loading data and models...")
        data1, data2 = load_data()
        
        # Test with a team pair that has historical data
        home_team = "Basel"
        away_team = "Young Boys"
        
        print(f"\n🏆 Testing: {home_team} vs {away_team}")
        
        # Run prediction
        prediction_result = run_prediction(home_team, away_team, None, data2, "v2")
        
        # Unpack the result
        final_prediction, full_confidence, probabilities, home_form, away_form, h2h_data, has_sufficient_data, insufficient_reasons = prediction_result
        
        print(f"✅ Final prediction: {final_prediction}")
        print(f"✅ Historical probabilities: {probabilities}")
        
        # Test the format conversion for web interface
        historical_probabilities = {}
        if probabilities:
            for outcome, prob in probabilities.items():
                if outcome == "Home Team Win":
                    historical_probabilities['Home'] = prob
                elif outcome == "Draw":
                    historical_probabilities['Draw'] = prob
                elif outcome == "Away Team Win":
                    historical_probabilities['Away'] = prob
        
        print(f"✅ Web format probabilities: {historical_probabilities}")
        
        # Test the Django template format
        template_probabilities = {}
        for outcome, prob in historical_probabilities.items():
            template_probabilities[outcome] = prob / 100.0  # Convert to decimal for template
        
        print(f"✅ Template format probabilities: {template_probabilities}")
        
        # Display the expected web output
        print(f"\n🎯 Expected Web Display:")
        print("🤖 Prediction Probabilities:")
        for outcome, prob in historical_probabilities.items():
            if outcome == "Home":
                print(f"  Home Win {prob:.1f}%")
            elif outcome == "Draw":
                print(f"  Draw {prob:.1f}%")
            elif outcome == "Away":
                print(f"  Away Win {prob:.1f}%")
        
        print("\n✅ Web probabilities test completed!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_web_probabilities() 