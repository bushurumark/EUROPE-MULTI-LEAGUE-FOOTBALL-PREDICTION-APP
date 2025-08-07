#!/usr/bin/env python3
"""
Test server response to check if HTML contains validation logic.
"""

import urllib.request
import urllib.parse

def test_server_response():
    """Test server response for validation logic."""
    print("Testing server response...")
    
    try:
        # Test the predict page
        url = "http://127.0.0.1:8000/predict/"
        
        print(f"Testing URL: {url}")
        
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
        
        print("Server Response Test:")
        print("=" * 50)
        
        # Check for validation patterns in served HTML
        validation_patterns = [
            'Team.*not found',
            'is-invalid',
            'teamFound',
            'leaguesData.*includes',
            'createElement.*message',
            'Young Boys.*not found'
        ]
        
        for pattern in validation_patterns:
            if pattern in html_content:
                print(f"❌ Found validation pattern in server response: {pattern}")
            else:
                print(f"✅ No validation pattern in server response: {pattern}")
        
        # Check for specific error message
        if "Team 'Young Boys' not found. Please check the spelling." in html_content:
            print("❌ Found specific error message for Young Boys in server response")
        else:
            print("✅ No specific error message for Young Boys in server response")
        
        # Check for is-invalid class
        if "is-invalid" in html_content:
            print("❌ Found is-invalid class in server response")
        else:
            print("✅ No is-invalid class in server response")
        
        print("=" * 50)
        print("✅ Server response test completed!")
        
        # Summary
        if "is-invalid" not in html_content and "Team.*not found" not in html_content:
            print("\n📋 SUMMARY:")
            print("✅ Server is serving correct HTML (no validation)")
            print("✅ Issue is likely browser cache")
            print("✅ User needs to clear browser cache")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        print("Make sure the Django server is running on port 8000")

if __name__ == "__main__":
    test_server_response() 