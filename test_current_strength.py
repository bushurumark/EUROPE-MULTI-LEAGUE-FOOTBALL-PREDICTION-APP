#!/usr/bin/env python3
"""
Test to check current strength calculations.
"""

import sys
import os
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_predictor.settings')
django.setup()

def test_current_strength():
    """Test current strength calculations."""
    print("Testing current strength calculations...")
    
    try:
        from analytics import analytics_engine
        
        test_teams = ['Fulham', 'Man City', 'Arsenal', 'Liverpool']
        
        print("Current Strength Test:")
        print("=" * 50)
        print(f"{'Team':<15} {'Home Strength':<15} {'Away Strength':<15}")
        print("-" * 50)
        
        for team in test_teams:
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
        
        # Check if we're getting varied values
        home_strengths = []
        away_strengths = []
        
        for team in test_teams:
            try:
                home_strength = analytics_engine.calculate_team_strength(team, 'home')
                away_strength = analytics_engine.calculate_team_strength(team, 'away')
                home_strengths.append(home_strength)
                away_strengths.append(away_strength)
            except:
                pass
        
        if len(home_strengths) > 1:
            home_variance = max(home_strengths) - min(home_strengths)
            away_variance = max(away_strengths) - min(away_strengths)
            
            print(f"\nVariance Analysis:")
            print(f"Home strength variance: {home_variance:.3f}")
            print(f"Away strength variance: {away_variance:.3f}")
            
            if home_variance > 0.05 and away_variance > 0.05:
                print("✅ Strength calculations are varied (good!)")
            else:
                print("❌ Strength calculations are too similar")
        else:
            print("❌ Not enough data to test variance")
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_current_strength() 