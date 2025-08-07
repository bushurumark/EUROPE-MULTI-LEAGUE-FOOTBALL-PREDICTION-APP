#!/usr/bin/env python3
"""
Simple debug script for analytics engine
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def debug_simple():
    """Simple debug for analytics engine"""
    
    print("🔍 Simple debug for analytics engine...")
    
    try:
        # Import analytics engine
        from analytics import analytics_engine
        
        print(f"📊 Analytics engine data available: {analytics_engine.data is not None}")
        
        if analytics_engine.data is not None:
            # Get first two teams from the dataset
            teams = analytics_engine.data['HomeTeam'].unique()
            team1 = teams[0]
            team2 = teams[1]
            
            print(f"🧪 Testing with: {team1} vs {team2}")
            
            # Test head-to-head stats directly
            h2h_stats = analytics_engine.get_head_to_head_stats(team1, team2)
            print(f"📊 H2H stats: {h2h_stats}")
            
            # Test historical probabilities
            result = analytics_engine.get_historical_probabilities(team1, team2)
            print(f"📊 Historical probabilities: {result}")
            
        else:
            print("❌ Analytics engine has no data")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_simple() 