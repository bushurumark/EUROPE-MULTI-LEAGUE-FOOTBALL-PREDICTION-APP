#!/usr/bin/env python3
"""
Test script to verify historical data API fixes
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analytics import analytics_engine

def test_historical_data():
    """Test the historical data functionality"""
    
    print("🔍 Testing Historical Data API...")
    
    # Test with Man United vs Newcastle
    team1 = "Man United"
    team2 = "Newcastle"
    
    print(f"📊 Testing: {team1} vs {team2}")
    
    try:
        # Test head-to-head stats
        h2h_stats = analytics_engine.get_head_to_head_stats(team1, team2)
        print(f"📈 H2H Stats: {h2h_stats}")
        
        # Test historical probabilities
        historical_data = analytics_engine.get_historical_probabilities(team1, team2)
        print(f"📊 Historical Data: {historical_data}")
        
        if historical_data:
            print("✅ Historical data API is working!")
            print(f"   - Total matches: {historical_data['total_matches']}")
            print(f"   - {team1} wins: {historical_data['team1_wins']}")
            print(f"   - {team2} wins: {historical_data['team2_wins']}")
            print(f"   - Draws: {historical_data['draws']}")
            print(f"   - Match history: {len(historical_data['match_history'])} matches")
        else:
            print("❌ No historical data found")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_historical_data() 