#!/usr/bin/env python3
"""
Test script to check historical API for unknown teams
"""

import requests
import json

def test_unknown_teams():
    """Test historical API with unknown teams"""
    
    print("🔍 Testing historical API with unknown teams...")
    
    # Test URL
    url = "http://127.0.0.1:8000/api/historical-probabilities/"
    
    # Test with teams that are NOT in the dataset
    params = {
        'team1': 'Viborg',
        'team2': 'Brondby'
    }
    
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
            
            print(f"\n📈 Historical Probabilities:")
            print(f"   {params['team1']} Win Rate: {data.get('team1_win_rate', 'N/A')}%")
            print(f"   {params['team2']} Win Rate: {data.get('team2_win_rate', 'N/A')}%")
            print(f"   Draw Rate: {data.get('draw_rate', 'N/A')}%")
            print(f"   Data Source: {data.get('data_source', 'N/A')}")
            
            if data.get('data_source') == 'simulated_data':
                print("❌ Using simulated data - teams not found in dataset")
            else:
                print("✅ Using real historical data")
        else:
            print(f"❌ Error! Response text:")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the Django server is running")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_unknown_teams() 