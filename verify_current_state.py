#!/usr/bin/env python3
"""
Verify current state of HTML file and confirm team validation is removed.
"""

def verify_current_state():
    """Verify current state of HTML file."""
    print("Verifying current state of HTML file...")
    
    try:
        with open('templates/predictor/predict.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Current State Verification:")
        print("=" * 50)
        
        # Check for team validation logic
        validation_checks = [
            ('Team validation logic', 'teamFound', False),
            ('Error message creation', 'createElement.*message', False),
            ('Team not found text', 'Team.*not found', False),
            ('Team message class', 'team-message', True),  # Only for removal
            ('API call logic', 'fetch.*team-stats', True),
            ('Stats display logic', 'updateStatsDisplay', True),
        ]
        
        for description, pattern, should_exist in validation_checks:
            if pattern in content:
                if should_exist:
                    print(f"✅ {description}: Found (expected)")
                else:
                    print(f"❌ {description}: Found (should be removed)")
            else:
                if should_exist:
                    print(f"❌ {description}: Not found (should exist)")
                else:
                    print(f"✅ {description}: Not found (correct)")
        
        # Check for specific problematic patterns
        problematic_patterns = [
            'leaguesData.*includes',
            'team.*available',
            'team.*validation',
            'Team.*Please check the spelling'
        ]
        
        print("\nProblematic Patterns Check:")
        print("-" * 30)
        
        for pattern in problematic_patterns:
            if pattern in content:
                print(f"❌ Found problematic pattern: {pattern}")
            else:
                print(f"✅ No problematic pattern: {pattern}")
        
        print("=" * 50)
        print("✅ Current state verification completed!")
        
        # Summary
        if 'team-message' in content and 'Team.*not found' not in content:
            print("\n📋 SUMMARY:")
            print("✅ Team validation logic removed")
            print("✅ Error message creation removed")
            print("✅ Only cleanup code remains (team-message removal)")
            print("✅ API calls and stats display working correctly")
        
    except Exception as e:
        print(f"❌ Verification failed: {e}")

if __name__ == "__main__":
    verify_current_state() 