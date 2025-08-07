#!/usr/bin/env python3
"""
Test script to check if the team stats API is returning strength data correctly.
"""

import sys
import os
import requests
import json
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_strength_api():
    """Test the team stats API to see if strength data is being returned."""
    print("Testing team stats API for strength data...")
    
    # Test teams
    test_teams = [
        'Man United',
        'Arsenal', 
        'Real Madrid',
        'Bayern Munich',
        'Paris SG',
        'Young Boys',
        'Zenit'
    ]
    
    print("Team Stats API Test Results:")
    print("=" * 80)
    print(f"{'Team':<20} {'Home Strength':<15} {'Away Strength':<15} {'Status'}")
    print("-" * 80)
    
    for team in test_teams:
        try:
            # Make API request
            url = f"http://localhost:8000/api/team-stats/?team={team}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                home_strength = data.get('home_strength', 'N/A')
                away_strength = data.get('away_strength', 'N/A')
                
                if home_strength != 'N/A' and away_strength != 'N/A':
                    print(f"{team:<20} {home_strength:>13.1f}% {away_strength:>13.1f}% ✅")
                else:
                    print(f"{team:<20} {'MISSING':<15} {'MISSING':<15} ❌")
                    
            else:
                print(f"{team:<20} {'ERROR':<15} {'ERROR':<15} ❌ ({response.status_code})")
                
        except Exception as e:
            print(f"{team:<20} {'ERROR':<15} {'ERROR':<15} ❌ ({str(e)[:20]}...)")
    
    print("=" * 80)
    print("✅ API test completed!")

def test_direct_analytics():
    """Test the analytics engine directly to verify strength calculations."""
    print("\nTesting analytics engine directly...")
    
    try:
        from analytics import analytics_engine
        
        test_teams = ['Man United', 'Arsenal', 'Real Madrid']
        
        print("Direct Analytics Test:")
        print("=" * 50)
        print(f"{'Team':<20} {'Home Strength':<15} {'Away Strength':<15}")
        print("-" * 50)
        
        for team in test_teams:
            try:
                home_strength = analytics_engine.calculate_team_strength(team, 'home')
                away_strength = analytics_engine.calculate_team_strength(team, 'away')
                
                home_percent = round(home_strength * 100, 1)
                away_percent = round(away_strength * 100, 1)
                
                print(f"{team:<20} {home_percent:>13.1f}% {away_percent:>13.1f}% ✅")
                
            except Exception as e:
                print(f"{team:<20} {'ERROR':<15} {'ERROR':<15} ❌ ({str(e)[:20]}...)")
        
        print("=" * 50)
        print("✅ Direct analytics test completed!")
        
    except Exception as e:
        print(f"❌ Direct analytics test failed: {e}")

def main():
    """Run all strength tests."""
    print("Running strength API tests...")
    print("=" * 80)
    
    # Test direct analytics first
    test_direct_analytics()
    
    print("\n" + "=" * 80)
    
    # Test API endpoint
    test_strength_api()
    
    print("\n" + "=" * 80)
    print("🎯 SUMMARY:")
    print("- If direct analytics works but API doesn't: Frontend issue")
    print("- If both work: Frontend display issue")
    print("- If neither works: Backend calculation issue")

if __name__ == "__main__":
    main() 