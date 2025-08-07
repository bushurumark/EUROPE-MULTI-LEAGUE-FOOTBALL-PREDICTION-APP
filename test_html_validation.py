#!/usr/bin/env python3
"""
Test to check if HTML file contains team validation logic.
"""

def test_html_validation():
    """Test if HTML file contains team validation logic."""
    print("Testing HTML file for team validation logic...")
    
    try:
        with open('templates/predictor/predict.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for common validation patterns
        validation_patterns = [
            'Team.*not found',
            'team.*found',
            'teamFound',
            'leaguesData.*includes',
            'createElement.*message',
            'team.*available',
            'team.*validation'
        ]
        
        print("HTML Validation Test:")
        print("=" * 50)
        
        for pattern in validation_patterns:
            if pattern in content:
                print(f"❌ Found validation pattern: {pattern}")
            else:
                print(f"✅ No validation pattern: {pattern}")
        
        # Check for specific error message
        if "Team 'Liverpool' not found. Please check the spelling." in content:
            print("❌ Found specific error message for Liverpool")
        else:
            print("✅ No specific error message for Liverpool")
        
        # Check for team message creation
        if "team-message" in content:
            print("❌ Found team-message class usage")
        else:
            print("✅ No team-message class usage")
        
        print("=" * 50)
        print("✅ HTML validation test completed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")

if __name__ == "__main__":
    test_html_validation() 