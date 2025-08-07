#!/usr/bin/env python3
"""
Test to check if historical probabilities align with user expectations
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_loader import load_data, download_models
from analytics import get_head_to_head_history, calculate_probabilities

def test_historical_alignment():
    """Test if historical probabilities align with expectations"""
    
    print("🔍 Testing Historical Probabilities Alignment")
    print("=" * 50)
    
    try:
        # Load data
        print("📊 Loading data...")
        data1, data2 = load_data()
        
        print(f"✅ Dataset 2 shape: {data2.shape}")
        
        # Test teams that should have historical data
        test_cases = [
            ("Basel", "Young Boys"),
            ("CFR Cluj", "Astra"),
            ("CSKA Moscow", "Dynamo Moscow")
        ]
        
        print("\n🇪🇺 Testing Historical Data Alignment")
        print("-" * 40)
        
        for team1, team2 in test_cases:
            print(f"\n🏆 Testing: {team1} vs {team2}")
            
            # Get head-to-head data
            h2h_data = get_head_to_head_history(team1, team2, data2, version="v2")
            
            if h2h_data is not None and not h2h_data.empty:
                print(f"✅ Found {len(h2h_data)} historical matches")
                
                # Calculate probabilities
                probs = calculate_probabilities(team1, team2, data2, version="v2")
                
                if probs:
                    print(f"📊 Historical Probabilities:")
                    for outcome, prob in probs.items():
                        if outcome == "Home Team Win":
                            print(f"  Home Win {prob:.1f}%")
                        elif outcome == "Draw":
                            print(f"  Draw {prob:.1f}%")
                        elif outcome == "Away Team Win":
                            print(f"  Away Win {prob:.1f}%")
                        else:
                            print(f"  {outcome} {prob:.1f}%")
                    
                    # Check if probabilities sum to ~100%
                    total = sum(probs.values())
                    print(f"📈 Total: {total:.1f}%")
                    
                    # Show sample matches
                    print(f"📋 Sample matches:")
                    for idx, row in h2h_data.head(3).iterrows():
                        date = row.get('Date', 'Unknown')
                        home = row.get('Home', 'Unknown')
                        away = row.get('Away', 'Unknown')
                        result = row.get('Res', 'Unknown')
                        print(f"    {date}: {home} vs {away} - {result}")
                else:
                    print(f"❌ No probabilities calculated")
            else:
                print(f"❌ No historical data found")
        
        # Test with your expected format
        print("\n🎯 Testing Your Expected Format")
        print("-" * 30)
        
        expected_probs = {
            "Home Team Win": 33.3,
            "Draw": 33.4,
            "Away Team Win": 33.3
        }
        
        print("🤖 Prediction Probabilities:")
        for outcome, prob in expected_probs.items():
            if outcome == "Home Team Win":
                print(f"  Home Win {prob:.1f}%")
            elif outcome == "Draw":
                print(f"  Draw {prob:.1f}%")
            elif outcome == "Away Team Win":
                print(f"  Away Win {prob:.1f}%")
            else:
                print(f"  {outcome} {prob:.1f}%")
        
        total_expected = sum(expected_probs.values())
        print(f"📈 Total: {total_expected:.1f}%")
        
        print("\n✅ Historical alignment test completed!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_historical_alignment() 