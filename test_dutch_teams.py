#!/usr/bin/env python3
"""
Test with Dutch teams that are in the dataset
"""

import requests
import json

def test_dutch_teams():
    """Test with Dutch teams that are in the dataset"""
    
    # Test URL
    url = "http://127.0.0.1:8000/api/historical-probabilities/"
    
    # Test with teams that are in the dataset
    params = {
        'team1': 'Groningen',
        'team2': 'Feyenoord'
    }
    
    print("🔍 Testing with Dutch teams...")
    print(f"📡 URL: {url}")
    print(f"📋 Parameters: {params}")
    
    try:
        # Make the request
        response = requests.get(url, params=params)
        
        print(f"📊 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success! Response data:")
            print(json.dumps(data, indent=2))
            
            if data['total_matches'] > 0:
                print("🎉 Found real historical data!")
            else:
                print("❌ Still no historical data found")
        else:
            print(f"❌ Error! Response text:")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the Django server is running")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_dutch_teams() 