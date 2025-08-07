#!/usr/bin/env python3
"""
Test script to debug prediction probabilities
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_prediction():
    """Test prediction probabilities"""
    
    print("🔍 Testing prediction probabilities...")
    
    try:
        # Import required modules
        from data_loader import download_models, load_data
        from controller import run_prediction
        
        # Load models and data
        print("📊 Loading models and data...")
        model1, model2 = download_models()
        data1, data2 = load_data()
        
        print(f"✅ Models loaded: {model1 is not None}, {model2 is not None}")
        print(f"✅ Data loaded: {data1 is not None}, shape: {data1.shape if data1 is not None else 'None'}")
        
        # Test with known teams
        home_team = "Groningen"
        away_team = "Feyenoord"
        
        print(f"🧪 Testing prediction: {home_team} vs {away_team}")
        
        # Run prediction
        result = run_prediction(home_team, away_team, model1, data1, "v1")
        
        if result:
            prediction, confidence, probabilities, home_form, away_form, h2h_data, has_sufficient_data, reasons = result
            
            print(f"📊 Prediction result:")
            print(f"   Prediction: {prediction}")
            print(f"   Confidence: {confidence}")
            print(f"   Probabilities: {probabilities}")
            print(f"   Home form: {home_form}")
            print(f"   Away form: {away_form}")
            print(f"   Has sufficient data: {has_sufficient_data}")
            print(f"   Reasons: {reasons}")
            
            if probabilities:
                print(f"📈 Probability breakdown:")
                for outcome, prob in probabilities.items():
                    print(f"   {outcome}: {prob:.1%}")
            else:
                print("❌ No probabilities returned")
        else:
            print("❌ No prediction result returned")
            
        # Test with unknown teams
        print(f"\n🧪 Testing with unknown teams: Viborg vs Brondby")
        result2 = run_prediction("Viborg", "Brondby", model1, data1, "v1")
        
        if result2:
            prediction2, confidence2, probabilities2, home_form2, away_form2, h2h_data2, has_sufficient_data2, reasons2 = result2
            
            print(f"📊 Unknown teams result:")
            print(f"   Prediction: {prediction2}")
            print(f"   Confidence: {confidence2}")
            print(f"   Probabilities: {probabilities2}")
            print(f"   Has sufficient data: {has_sufficient_data2}")
            print(f"   Reasons: {reasons2}")
            
            if probabilities2:
                print(f"📈 Unknown teams probability breakdown:")
                for outcome, prob in probabilities2.items():
                    print(f"   {outcome}: {prob:.1%}")
        else:
            print("❌ No prediction result for unknown teams")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_prediction() 