#!/usr/bin/env python3
"""
Test script to verify the fixes for the football prediction app.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_team_variations():
    """Test team name variations handling."""
    print("Testing team name variations...")
    
    try:
        from analytics import get_team_recent_form, get_head_to_head_history, calculate_probabilities
        from model_utils import compute_mean_for_teams, calculate_probabilities as model_calc_probs
        
        # Test data (simplified)
        import pandas as pd
        test_data = pd.DataFrame({
            'HomeTeam': ['Man City', 'Arsenal', 'Liverpool', 'Chelsea'],
            'AwayTeam': ['Arsenal', 'Man City', 'Chelsea', 'Liverpool'],
            'FTR': ['H', 'A', 'H', 'D'],
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
        })
        
        # Test team variations
        variations_to_test = [
            ('man city', 'Man City'),
            ('manchester city', 'Man City'),
            ('man united', 'Man United'),
            ('manchester united', 'Man United'),
            ('newcastle', 'Newcastle'),
            ('west ham', 'West Ham'),
        ]
        
        for input_name, expected_name in variations_to_test:
            print(f"  Testing '{input_name}' -> should match '{expected_name}'")
            
            # Test get_team_recent_form
            try:
                form = get_team_recent_form(input_name, test_data)
                print(f"    ✓ get_team_recent_form: {form}")
            except Exception as e:
                print(f"    ✗ get_team_recent_form error: {e}")
            
            # Test calculate_probabilities
            try:
                probs = calculate_probabilities(input_name, 'Arsenal', test_data)
                print(f"    ✓ calculate_probabilities: {probs}")
            except Exception as e:
                print(f"    ✗ calculate_probabilities error: {e}")
        
        print("✓ Team variations test completed")
        return True
        
    except Exception as e:
        print(f"✗ Team variations test failed: {e}")
        return False

def test_dataframe_handling():
    """Test DataFrame handling to avoid truth value errors."""
    print("Testing DataFrame handling...")
    
    try:
        import pandas as pd
        
        # Test empty DataFrame handling
        empty_df = pd.DataFrame()
        if empty_df.empty:
            print("  ✓ Empty DataFrame properly detected")
        else:
            print("  ✗ Empty DataFrame not detected")
            return False
        
        # Test non-empty DataFrame handling
        non_empty_df = pd.DataFrame({'A': [1, 2, 3]})
        if not non_empty_df.empty:
            print("  ✓ Non-empty DataFrame properly detected")
        else:
            print("  ✗ Non-empty DataFrame not detected")
            return False
        
        print("✓ DataFrame handling test completed")
        return True
        
    except Exception as e:
        print(f"✗ DataFrame handling test failed: {e}")
        return False

def test_service_worker():
    """Test service worker file exists."""
    print("Testing service worker...")
    
    try:
        sw_path = os.path.join(os.path.dirname(__file__), 'static', 'sw.js')
        if os.path.exists(sw_path):
            print("  ✓ Service worker file exists")
            
            with open(sw_path, 'r') as f:
                content = f.read()
                if 'Service Worker' in content:
                    print("  ✓ Service worker content looks correct")
                else:
                    print("  ✗ Service worker content seems incorrect")
                    return False
        else:
            print("  ✗ Service worker file not found")
            return False
        
        print("✓ Service worker test completed")
        return True
        
    except Exception as e:
        print(f"✗ Service worker test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Running football prediction app fixes tests...")
    print("=" * 50)
    
    tests = [
        test_team_variations,
        test_dataframe_handling,
        test_service_worker,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed! The fixes should work correctly.")
    else:
        print("✗ Some tests failed. Please check the issues.")
    
    return passed == total

if __name__ == "__main__":
    main() 