#!/usr/bin/env python3
"""
Test script for historical probabilities API
"""

import requests
import json

def test_historical_api():
    """Test the historical probabilities API endpoint"""
    
    # Test URL
    url = "http://127.0.0.1:8000/api/historical-probabilities/"
    
    # Test parameters
    params = {
        'team1': 'Man United',
        'team2': 'Newcastle'
    }
    
    print("🔍 Testing Historical Probabilities API...")
    print(f"📡 URL: {url}")
    print(f"📋 Parameters: {params}")
    
    try:
        # Make the request
        response = requests.get(url, params=params)
        
        print(f"📊 Response Status: {response.status_code}")
        print(f"📄 Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success! Response data:")
            print(json.dumps(data, indent=2))
        else:
            print(f"❌ Error! Response text:")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the Django server is running")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_historical_api() 