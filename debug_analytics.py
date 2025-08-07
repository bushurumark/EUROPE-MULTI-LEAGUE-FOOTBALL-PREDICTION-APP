#!/usr/bin/env python3
"""
Debug script for analytics engine
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def debug_analytics():
    """Debug the analytics engine"""
    
    print("🔍 Debugging Analytics Engine...")
    
    try:
        # Test data loading
        from data_loader import load_data
        data1, data2 = load_data()
        print(f"✅ Data loaded successfully")
        print(f"📊 Data1 shape: {data1.shape}")
        print(f"📊 Data2 shape: {data2.shape}")
        
        # Check column names
        print(f"📋 Data1 columns: {list(data1.columns)}")
        print(f"📋 Sample HomeTeam values: {data1['HomeTeam'].unique()[:10]}")
        
        # Test analytics engine
        from analytics import analytics_engine
        print(f"📊 Analytics engine data available: {analytics_engine.data is not None}")
        
        if analytics_engine.data is not None:
            print(f"📈 Analytics data shape: {analytics_engine.data.shape}")
            print(f"🏟️ Available teams: {list(analytics_engine.data['HomeTeam'].unique())[:10]}")
            
            # Test with a team that should exist
            test_team = analytics_engine.data['HomeTeam'].iloc[0]
            print(f"🧪 Testing with team: {test_team}")
            
            # Test head-to-head
            from analytics import get_head_to_head_history
            h2h = get_head_to_head_history(test_team, analytics_engine.data['AwayTeam'].iloc[0], analytics_engine.data)
            print(f"📊 H2H result: {len(h2h)} matches found")
            
        else:
            print("❌ Analytics engine has no data")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_analytics() 