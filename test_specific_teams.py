#!/usr/bin/env python3
"""
Test script to check specific teams mentioned by user
"""

import requests
import json

def test_specific_teams():
    """Test historical API with specific teams mentioned by user"""
    
    print("🔍 Testing historical API with specific teams...")
    
    # Test URL
    url = "http://127.0.0.1:8000/api/historical-probabilities/"
    
    # Test with the specific teams mentioned by user
    test_cases = [
        ('Viborg', 'Brondby'),
        ('Yverdon', 'Lausanne'),
        ('Groningen', 'Feyenoord')  # Known teams for comparison
    ]
    
    for team1, team2 in test_cases:
        print(f"\n🧪 Testing: {team1} vs {team2}")
        
        params = {
            'team1': team1,
            'team2': team2
        }
        
        try:
            # Make the request
            response = requests.get(url, params=params)
            
            print(f"📊 Response Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Success! Data source: {data.get('data_source', 'N/A')}")
                print(f"📈 Historical Probabilities:")
                print(f"   {team1} Win Rate: {data.get('team1_win_rate', 'N/A')}%")
                print(f"   {team2} Win Rate: {data.get('team2_win_rate', 'N/A')}%")
                print(f"   Draw Rate: {data.get('draw_rate', 'N/A')}%")
                print(f"   Total Matches: {data.get('total_matches', 'N/A')}")
                
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
    test_specific_teams() 