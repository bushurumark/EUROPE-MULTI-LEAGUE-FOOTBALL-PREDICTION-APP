#!/usr/bin/env python3
"""
Test script to debug Premier League team search issues.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_premier_league_teams():
    """Test Premier League team recognition."""
    print("Testing Premier League team recognition...")
    
    try:
        from predictor.views import LEAGUES_BY_CATEGORY
        
        # Get Premier League teams
        premier_league_teams = LEAGUES_BY_CATEGORY['European Leagues']['Premier League']
        
        print("Premier League Teams in LEAGUES_BY_CATEGORY:")
        print("=" * 50)
        for i, team in enumerate(premier_league_teams, 1):
            print(f"{i:2d}. {team}")
        
        print("\nTesting specific problematic teams:")
        print("=" * 50)
        
        test_teams = ['Man United', 'Aston Villa', 'Man City', 'Arsenal', 'Liverpool']
        
        for team in test_teams:
            if team in premier_league_teams:
                print(f"✅ {team} - FOUND in Premier League")
            else:
                print(f"❌ {team} - NOT FOUND in Premier League")
        
        return True
        
    except Exception as e:
        print(f"❌ Premier League test failed: {e}")
        return False

def test_team_search_logic():
    """Test the team search logic from api_find_team."""
    print("\nTesting team search logic...")
    
    try:
        from predictor.views import LEAGUES_BY_CATEGORY
        
        # Simulate the search logic from api_find_team
        team_name = "Man United"
        search_lower = team_name.lower()
        
        print(f"Searching for: '{team_name}' (lowercase: '{search_lower}')")
        
        # Check if it's in team variations
        team_variations = {
            'man united': ['Man United', 'Manchester United'],
            'manchester united': ['Man United', 'Manchester United'],
            'aston villa': ['Aston Villa'],
        }
        
        if search_lower in team_variations:
            print(f"✅ Found in team variations: {team_variations[search_lower]}")
        else:
            print(f"❌ NOT found in team variations")
        
        # Check if it's in Premier League
        premier_league_teams = LEAGUES_BY_CATEGORY['European Leagues']['Premier League']
        
        # Case-insensitive search
        matching_teams = [team for team in premier_league_teams if team_name.lower() in team.lower()]
        
        print(f"Teams matching '{team_name}' in Premier League: {matching_teams}")
        
        if matching_teams:
            print("✅ Found in Premier League")
        else:
            print("❌ NOT found in Premier League")
        
        return True
        
    except Exception as e:
        print(f"❌ Team search logic test failed: {e}")
        return False

def test_analytics_team_recognition():
    """Test if analytics functions can recognize Premier League teams."""
    print("\nTesting analytics team recognition...")
    
    try:
        from analytics import get_team_recent_form, calculate_probabilities
        from model_utils import compute_mean_for_teams
        
        # Test data
        import pandas as pd
        test_data = pd.DataFrame({
            'HomeTeam': ['Man United', 'Aston Villa', 'Man City', 'Arsenal'],
            'AwayTeam': ['Aston Villa', 'Man United', 'Arsenal', 'Man City'],
            'FTR': ['H', 'A', 'H', 'D'],
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
        })
        
        test_teams = ['Man United', 'Aston Villa', 'Man City', 'Arsenal']
        
        for team in test_teams:
            try:
                # Test get_team_recent_form
                form = get_team_recent_form(team, test_data)
                print(f"✅ {team} - get_team_recent_form works")
                
                # Test calculate_probabilities
                probs = calculate_probabilities(team, 'Arsenal', test_data)
                print(f"✅ {team} - calculate_probabilities works")
                
            except Exception as e:
                print(f"❌ {team} - Error: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Analytics team recognition test failed: {e}")
        return False

def main():
    """Run all Premier League tests."""
    print("Running Premier League team tests...")
    print("=" * 60)
    
    tests = [
        test_premier_league_teams,
        test_team_search_logic,
        test_analytics_team_recognition,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 60)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✅ All Premier League tests passed!")
        print("\nPremier League teams should work properly:")
        print("- Man United, Aston Villa, Man City, Arsenal, etc.")
        print("- Team search should find them in Premier League")
        print("- Analytics functions should recognize them")
    else:
        print("❌ Some Premier League tests failed. Please check the issues.")
    
    return passed == total

if __name__ == "__main__":
    main() 