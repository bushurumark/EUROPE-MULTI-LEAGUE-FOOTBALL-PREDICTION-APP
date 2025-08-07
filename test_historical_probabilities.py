#!/usr/bin/env python3
"""
Test script to check historical probabilities functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_loader import load_data, download_models
from analytics import AnalyticsEngine

def test_historical_probabilities():
    """Test historical probabilities with European teams"""
    
    print("🔍 Testing Historical Probabilities")
    print("=" * 50)
    
    try:
        # Load data and models
        print("📊 Loading data and models...")
        data1, data2 = load_data()
        model1, model2 = download_models()
        
        print(f"✅ Dataset 1 shape: {data1.shape}")
        print(f"✅ Dataset 2 shape: {data2.shape}")
        
        # Test with European teams from dataset 2
        print("\n🇪🇺 Testing European Teams (Dataset 2)")
        print("-" * 40)
        
        # Initialize analytics engine with dataset 2
        analytics_engine = AnalyticsEngine()
        analytics_engine.data = data2
        
        # Test teams that should be in dataset 2
        test_cases = [
            ("Barcelona", "Real Madrid"),
            ("Bayern Munich", "Dortmund"),
            ("PSG", "Marseille"),
            ("Juventus", "Milan"),
            ("Porto", "Benfica"),
            ("Ajax", "PSV"),
            ("Basel", "Young Boys"),
            ("Atalanta", "Inter")
        ]
        
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
        print("-" * 40)
        
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
        
        print("\n✅ Historical probabilities test completed!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_historical_probabilities() 