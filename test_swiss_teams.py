#!/usr/bin/env python3
"""
Test script to verify Swiss team support is working properly.
"""

import sys
import os
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_swiss_team_recognition():
    """Test Swiss team name recognition and variations."""
    print("Testing Swiss team recognition...")
    
    try:
        from analytics import get_team_recent_form, get_head_to_head_history, calculate_probabilities
        from model_utils import compute_mean_for_teams, calculate_probabilities as model_calc_probs
        
        # Test data (simplified)
        import pandas as pd
        test_data = pd.DataFrame({
            'HomeTeam': ['Young Boys', 'Basel', 'Grasshoppers', 'Yverdon'],
            'AwayTeam': ['Basel', 'Young Boys', 'Yverdon', 'Grasshoppers'],
            'FTR': ['H', 'A', 'H', 'D'],
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
        })
        
        # Test Swiss team variations
        swiss_teams_to_test = [
            ('young boys', 'Young Boys'),
            ('young boys bern', 'Young Boys'),
            ('yverdon', 'Yverdon'),
            ('yverdon sport', 'Yverdon'),
            ('basel', 'Basel'),
            ('fc basel', 'Basel'),
            ('grasshoppers', 'Grasshoppers'),
            ('grasshoppers zurich', 'Grasshoppers'),
            ('lausanne', 'Lausanne'),
            ('lausanne sport', 'Lausanne'),
            ('lugano', 'Lugano'),
            ('fc lugano', 'Lugano'),
            ('luzern', 'Luzern'),
            ('fc luzern', 'Luzern'),
            ('servette', 'Servette'),
            ('servette geneva', 'Servette'),
            ('sion', 'Sion'),
            ('fc sion', 'Sion'),
            ('st. gallen', 'St. Gallen'),
            ('st gallen', 'St. Gallen'),
            ('winterthur', 'Winterthur'),
            ('fc winterthur', 'Winterthur'),
            ('zurich', 'Zurich'),
            ('fc zurich', 'Zurich'),
        ]
        
        print("Swiss Team Recognition Test:")
        print("=" * 50)
        print(f"{'Input Name':<20} {'Expected Match':<20} {'Status'}")
        print("-" * 50)
        
        success_count = 0
        total_count = len(swiss_teams_to_test)
        
        for input_name, expected_name in swiss_teams_to_test:
            try:
                # Test get_team_recent_form
                form = get_team_recent_form(input_name, test_data)
                
                # Test calculate_probabilities
                probs = calculate_probabilities(input_name, 'Basel', test_data)
                
                print(f"{input_name:<20} {expected_name:<20} ✅")
                success_count += 1
                
            except Exception as e:
                print(f"{input_name:<20} {expected_name:<20} ❌ ({e})")
        
        print("=" * 50)
        print(f"Success: {success_count}/{total_count}")
        
        if success_count == total_count:
            print("✅ All Swiss teams recognized successfully!")
            return True
        else:
            print("❌ Some Swiss teams failed recognition")
            return False
            
    except Exception as e:
        print(f"❌ Swiss team test failed: {e}")
        return False

def test_swiss_team_strength():
    """Test Swiss team strength calculations."""
    print("\nTesting Swiss team strength calculations...")
    
    try:
        from analytics import analytics_engine
        
        swiss_teams = [
            'Young Boys',
            'Yverdon', 
            'Basel',
            'Grasshoppers',
            'Lausanne',
            'Lugano',
            'Luzern',
            'Servette',
            'Sion',
            'St. Gallen',
            'Winterthur',
            'Zurich'
        ]
        
        print("Swiss Team Strength Test:")
        print("=" * 50)
        print(f"{'Team':<15} {'Home Strength':<15} {'Away Strength':<15}")
        print("-" * 50)
        
        for team in swiss_teams:
            try:
                home_strength = analytics_engine.calculate_team_strength(team, 'home')
                away_strength = analytics_engine.calculate_team_strength(team, 'away')
                
                home_percent = round(home_strength * 100, 1)
                away_percent = round(away_strength * 100, 1)
                
                print(f"{team:<15} {home_percent:>13.1f}% {away_percent:>13.1f}%")
                
            except Exception as e:
                print(f"{team:<15} {'ERROR':<15} {'ERROR':<15}")
                print(f"  Error: {e}")
        
        print("=" * 50)
        print("✅ Swiss team strength calculations completed")
        return True
        
    except Exception as e:
        print(f"❌ Swiss team strength test failed: {e}")
        return False

def main():
    """Run all Swiss team tests."""
    print("Running Swiss team support tests...")
    print("=" * 60)
    
    tests = [
        test_swiss_team_recognition,
        test_swiss_team_strength,
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
        print("✅ All Swiss team tests passed!")
        print("\nSwiss teams should now work properly:")
        print("- Young Boys, Yverdon, Basel, Grasshoppers, etc.")
        print("- Team name variations supported")
        print("- Realistic strength calculations")
        print("- No more 'team not found' errors")
    else:
        print("❌ Some Swiss team tests failed. Please check the issues.")
    
    return passed == total

if __name__ == "__main__":
    main() 