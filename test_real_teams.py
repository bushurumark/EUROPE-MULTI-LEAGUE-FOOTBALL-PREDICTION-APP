#!/usr/bin/env python3
"""
Test script to check historical probabilities with real teams from dataset 2
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_loader import load_data, download_models
from analytics import AnalyticsEngine
import pandas as pd

def test_real_teams():
    """Test historical probabilities with teams that actually exist in dataset 2"""
    
    print("🔍 Testing Historical Probabilities with Real Teams")
    print("=" * 60)
    
    try:
        # Load data and models
        print("📊 Loading data and models...")
        data1, data2 = load_data()
        model1, model2 = download_models()
        
        print(f"✅ Dataset 2 shape: {data2.shape}")
        
        # Get some real teams from dataset 2
        real_teams = sorted(data2['Home'].unique())[:20]
        print(f"📋 Sample teams in dataset: {real_teams}")
        
        # Test with teams that are actually in the dataset
        test_cases = [
            ("Basel", "Young Boys"),
            ("CFR Cluj", "Astra"),
            ("CSKA Moscow", "Dynamo Moscow"),
            ("Austria Vienna", "Admira"),
            ("Brondby", "Aalborg"),
            ("Akhmat Grozny", "Krasnodar")
        ]
        
        # Initialize analytics engine with dataset 2
        analytics_engine = AnalyticsEngine()
        analytics_engine.data = data2
        
        print("\n🇪🇺 Testing Real European Teams (Dataset 2)")
        print("-" * 50)
        
        for team1, team2 in test_cases:
            print(f"\n🏆 Testing: {team1} vs {team2}")
            
            # Get historical probabilities
            hist_probs = analytics_engine.get_historical_probabilities(team1, team2)
            
            if hist_probs:
                print(f"✅ Historical data found!")
                print(f"   Total matches: {hist_probs.get('total_matches', 0)}")
                print(f"   {team1} wins: {hist_probs.get('team1_wins', 0)}")
                print(f"   {team2} wins: {hist_probs.get('team2_wins', 0)}")
                print(f"   Draws: {hist_probs.get('draws', 0)}")
                print(f"   {team1} win rate: {hist_probs.get('team1_win_rate', 0)}%")
                print(f"   {team2} win rate: {hist_probs.get('team2_win_rate', 0)}%")
                print(f"   Draw rate: {hist_probs.get('draw_rate', 0)}%")
                
                # Check recent form
                recent_form = hist_probs.get('recent_form', {})
                if recent_form:
                    print(f"   Recent form:")
                    print(f"     {team1}: {recent_form.get('team1', [])}")
                    print(f"     {team2}: {recent_form.get('team2', [])}")
        else:
                print(f"❌ No historical data found for {team1} vs {team2}")
        
        # Test head-to-head history function directly
        print("\n🔍 Testing Head-to-Head History Function")
        print("-" * 50)
        
        from analytics import get_head_to_head_history
        
        for team1, team2 in test_cases[:3]:  # Test first 3 pairs
            print(f"\n📊 Head-to-head: {team1} vs {team2}")
            h2h_data = get_head_to_head_history(team1, team2, data2, version="v2")
            
            if h2h_data is not None and not h2h_data.empty:
                print(f"✅ Found {len(h2h_data)} matches")
                print(f"   Columns: {list(h2h_data.columns)}")
                print(f"   Sample data:")
                for idx, row in h2h_data.head(3).iterrows():
                    print(f"     {row.get('Date', 'Unknown')}: {row.get('Home', 'Unknown')} vs {row.get('Away', 'Unknown')} - {row.get('Res', 'Unknown')}")
            else:
                print(f"❌ No head-to-head data found")
        
        # Test model 2 prediction
        print("\n🤖 Testing Model 2 Prediction")
        print("-" * 50)
        
        from model_utils import get_prediction_summary
        
        for team1, team2 in test_cases[:2]:  # Test first 2 pairs
            print(f"\n🎯 Model prediction: {team1} vs {team2}")
            try:
                result = get_prediction_summary(team1, team2, model2, data2, version="v2")
                
                if result and 'error' not in result:
                    print(f"✅ Prediction successful!")
                    print(f"   Model prediction: {result.get('model_prediction', 'Unknown')}")
                    print(f"   Model confidence: {result.get('model_confidence', 0):.2f}")
                    print(f"   Final prediction: {result.get('final_prediction', 'Unknown')}")
                    print(f"   Data available: {result.get('data_available', False)}")
                    
                    # Check historical probabilities
                    hist_probs = result.get('historical_probabilities', {})
                    if hist_probs:
                        print(f"   Historical probabilities:")
                        for outcome, prob in hist_probs.items():
                            print(f"     {outcome}: {prob:.1f}%")
                else:
                    print(f"❌ Prediction failed: {result.get('error', 'Unknown error')}")
            except Exception as e:
                print(f"❌ Error in prediction: {e}")
        
        print("\n✅ Real teams test completed!")
            
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_real_teams() 