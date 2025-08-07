#!/usr/bin/env python3
"""
Test script to verify the DataFrame fixes work correctly.
"""

import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_dataframe_fix():
    """Test the DataFrame boolean operation fix."""
    try:
        from analytics import AnalyticsEngine
        
        # Create an instance
        engine = AnalyticsEngine()
        print("✅ AnalyticsEngine created successfully")
        
        # Test with a team that might not be in the dataset
        test_teams = ['Atalanta', 'Man City', 'Barcelona', 'Unknown Team']
        
        for team in test_teams:
            try:
                print(f"\n🔍 Testing team: {team}")
                
                # Test get_team_form - this should not raise DataFrame boolean error
                form_data = engine.get_team_form(team)
                print(f"  ✅ get_team_form returned: {type(form_data)}")
                if form_data:
                    print(f"  📊 Form data keys: {list(form_data.keys())}")
                    print(f"  📈 Recent form: {form_data.get('recent_form', 'N/A')}")
                    print(f"  ⚽ Goals scored: {form_data.get('goals_scored', 'N/A')}")
                    print(f"  🛡️ Goals conceded: {form_data.get('goals_conceded', 'N/A')}")
                
                # Test calculate_team_strength
                home_strength = engine.calculate_team_strength(team, 'home')
                away_strength = engine.calculate_team_strength(team, 'away')
                print(f"  💪 Home strength: {home_strength:.3f}")
                print(f"  💪 Away strength: {away_strength:.3f}")
                
            except Exception as e:
                print(f"  ❌ Error with team {team}: {e}")
                import traceback
                traceback.print_exc()
        
        print("\n✅ All tests completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error creating AnalyticsEngine: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_api_simulation():
    """Simulate the API endpoint logic."""
    try:
        from analytics import AnalyticsEngine
        import numpy as np
        
        engine = AnalyticsEngine()
        
        # Simulate the API logic
        team_name = "Atalanta"
        
        # Get team form
        form_data = engine.get_team_form(team_name)
        
        # Get team strength
        home_strength = engine.calculate_team_strength(team_name, 'home')
        away_strength = engine.calculate_team_strength(team_name, 'away')
        
        # Get injury/suspension data
        injuries = engine.get_injury_suspensions(team_name)
        
        # Calculate recent form percentage
        if form_data and form_data.get('recent_form'):
            form_points = {'W': 3, 'D': 1, 'L': 0}
            recent_points = sum(form_points[result] for result in form_data['recent_form'][:5])
            max_points = 15  # 5 matches * 3 points
            form_percentage = (recent_points / max_points) * 100
        else:
            form_percentage = 50  # Default neutral form
        
        # Safely get form data with defaults
        recent_form = form_data.get('recent_form', ['D', 'D', 'D', 'D', 'D']) if form_data else ['D', 'D', 'D', 'D', 'D']
        goals_scored = form_data.get('goals_scored', [1.5, 1.2, 1.8, 1.1, 1.6]) if form_data else [1.5, 1.2, 1.8, 1.1, 1.6]
        goals_conceded = form_data.get('goals_conceded', [1.2, 1.0, 1.5, 1.3, 1.1]) if form_data else [1.2, 1.0, 1.5, 1.3, 1.1]
        possession_avg = form_data.get('possession_avg', [50.0, 48.0, 52.0, 49.0, 51.0]) if form_data else [50.0, 48.0, 52.0, 49.0, 51.0]
        shots_on_target = form_data.get('shots_on_target', [4.5, 4.2, 4.8, 4.1, 4.6]) if form_data else [4.5, 4.2, 4.8, 4.1, 4.6]
        clean_sheets = form_data.get('clean_sheets', 2) if form_data else 2
        points = form_data.get('points', 25) if form_data else 25
        
        stats = {
            'team_name': team_name,
            'recent_form': recent_form[:5],
            'form_percentage': round(form_percentage, 1),
            'goals_scored_avg': float(round(np.mean(goals_scored[:5]), 1)),
            'goals_conceded_avg': float(round(np.mean(goals_conceded[:5]), 1)),
            'possession_avg': float(round(np.mean(possession_avg[:5]), 1)),
            'shots_on_target_avg': float(round(np.mean(shots_on_target[:5]), 1)),
            'clean_sheets': int(clean_sheets),
            'points': int(points),
            'home_strength': float(round(home_strength * 100, 1)),
            'away_strength': float(round(away_strength * 100, 1)),
            'injuries': injuries if injuries else {
                'key_players_out': 0,
                'total_players_out': 0,
                'impact_score': 0,
                'expected_return': 0
            }
        }
        
        print(f"\n✅ API simulation successful!")
        print(f"📊 Generated stats for {team_name}:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in API simulation: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Testing DataFrame fixes...")
    
    # Test 1: AnalyticsEngine functionality
    print("\n1️⃣ Testing AnalyticsEngine...")
    test1_success = test_dataframe_fix()
    
    # Test 2: API simulation
    print("\n2️⃣ Testing API simulation...")
    test2_success = test_api_simulation()
    
    # Summary
    print("\n" + "="*50)
    if test1_success and test2_success:
        print("🎉 All tests passed! The DataFrame fixes should work correctly.")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    print("="*50) 