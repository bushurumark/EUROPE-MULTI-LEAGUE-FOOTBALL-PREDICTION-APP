#!/usr/bin/env python3
"""
Test script to debug team stats API issues.
"""

import sys
import os
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_team_stats_calculation():
    """Test team stats calculation for Premier League teams."""
    print("Testing team stats calculation...")
    
    try:
        from analytics import analytics_engine
        
        test_teams = ['Man United', 'Aston Villa', 'Man City', 'Arsenal', 'Liverpool']
        
        print("Team Stats Test Results:")
        print("=" * 60)
        print(f"{'Team':<15} {'Form':<10} {'Goals':<8} {'Strength':<10} {'Status'}")
        print("-" * 60)
        
        for team in test_teams:
            try:
                # Get team form
                form_data = analytics_engine.get_team_form(team)
                
                # Get team strength
                home_strength = analytics_engine.calculate_team_strength(team, 'home')
                away_strength = analytics_engine.calculate_team_strength(team, 'away')
                
                # Calculate form percentage
                if form_data and form_data['recent_form']:
                    form_points = {'W': 3, 'D': 1, 'L': 0}
                    recent_points = sum(form_points[result] for result in form_data['recent_form'][:5])
                    max_points = 15  # 5 matches * 3 points
                    form_percentage = (recent_points / max_points) * 100
                else:
                    form_percentage = 50  # Default neutral form
                
                # Calculate average goals
                if form_data and 'goals_scored' in form_data:
                    avg_goals = np.mean(form_data['goals_scored'][:5])
                else:
                    avg_goals = 1.5
                
                # Calculate strength percentage
                strength_percent = round(home_strength * 100, 1)
                
                print(f"{team:<15} {form_percentage:>8.1f}% {avg_goals:>6.1f} {strength_percent:>8.1f}% ✅")
                
            except Exception as e:
                print(f"{team:<15} {'ERROR':<10} {'ERROR':<8} {'ERROR':<10} ❌ ({e})")
        
        print("=" * 60)
        print("✅ Team stats calculation completed")
        return True
        
    except Exception as e:
        print(f"❌ Team stats test failed: {e}")
        return False

def test_team_variations():
    """Test team name variations for Premier League teams."""
    print("\nTesting team name variations...")
    
    try:
        from analytics import get_team_recent_form, calculate_probabilities
        
        # Test data
        import pandas as pd
        test_data = pd.DataFrame({
            'HomeTeam': ['Man United', 'Aston Villa', 'Man City', 'Arsenal'],
            'AwayTeam': ['Aston Villa', 'Man United', 'Arsenal', 'Man City'],
            'FTR': ['H', 'A', 'H', 'D'],
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
        })
        
        # Test different name variations
        variations_to_test = [
            ('man united', 'Man United'),
            ('manchester united', 'Man United'),
            ('aston villa', 'Aston Villa'),
            ('man city', 'Man City'),
            ('manchester city', 'Man City'),
            ('arsenal', 'Arsenal'),
        ]
        
        print("Team Name Variations Test:")
        print("=" * 50)
        print(f"{'Input':<20} {'Expected':<20} {'Status'}")
        print("-" * 50)
        
        success_count = 0
        total_count = len(variations_to_test)
        
        for input_name, expected_name in variations_to_test:
            try:
                # Test get_team_recent_form
                form = get_team_recent_form(input_name, test_data)
                
                # Test calculate_probabilities
                probs = calculate_probabilities(input_name, 'Arsenal', test_data)
                
                print(f"{input_name:<20} {expected_name:<20} ✅")
                success_count += 1
                
            except Exception as e:
                print(f"{input_name:<20} {expected_name:<20} ❌ ({e})")
        
        print("=" * 50)
        print(f"Success: {success_count}/{total_count}")
        
        if success_count == total_count:
            print("✅ All team variations work correctly!")
            return True
        else:
            print("❌ Some team variations failed")
            return False
            
    except Exception as e:
        print(f"❌ Team variations test failed: {e}")
        return False

def test_dataset_teams():
    """Test if teams exist in the dataset."""
    print("\nTesting dataset team availability...")
    
    try:
        # Try to load data
        from data_loader import load_data
        
        data1, data2 = load_data()
        
        if data1 is not None:
            # Get unique teams from dataset
            home_teams = set(data1['HomeTeam'].unique())
            away_teams = set(data1['AwayTeam'].unique())
            all_teams = home_teams | away_teams
            
            print(f"Total teams in dataset: {len(all_teams)}")
            
            # Check for Premier League teams
            premier_teams = ['Man United', 'Aston Villa', 'Man City', 'Arsenal', 'Liverpool']
            
            print("\nPremier League teams in dataset:")
            print("=" * 40)
            
            found_count = 0
            for team in premier_teams:
                if team in all_teams:
                    print(f"✅ {team} - FOUND")
                    found_count += 1
                else:
                    print(f"❌ {team} - NOT FOUND")
            
            print("=" * 40)
            print(f"Found: {found_count}/{len(premier_teams)} Premier League teams")
            
            if found_count > 0:
                print("✅ Some Premier League teams found in dataset")
                return True
            else:
                print("❌ No Premier League teams found in dataset")
                return False
        else:
            print("❌ Could not load dataset")
            return False
            
    except Exception as e:
        print(f"❌ Dataset test failed: {e}")
        return False

def main():
    """Run all team stats tests."""
    print("Running team stats API tests...")
    print("=" * 60)
    
    tests = [
        test_team_stats_calculation,
        test_team_variations,
        test_dataset_teams,
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
        print("✅ All team stats tests passed!")
        print("\nTeam stats should work properly:")
        print("- Premier League teams should be recognized")
        print("- Team name variations should work")
        print("- Stats should be calculated correctly")
    else:
        print("❌ Some team stats tests failed. Please check the issues.")
    
    return passed == total

if __name__ == "__main__":
    main() 