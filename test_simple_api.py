#!/usr/bin/env python3
"""
Test script for the simplified API endpoint
"""

import requests
import time

def test_simple_api():
    """Test the simplified API endpoint"""
    
    # Wait a moment for server to start
    time.sleep(2)
    
    # Test data
    data = {
        'home_team': 'Man City',
        'away_team': 'Liverpool',
        'category': 'Premier League'
    }
    
    try:
        print("Testing simplified API endpoint...")
        response = requests.post('http://localhost:8000/api/predict-simple/', data=data, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ Simplified API is working!")
            result = response.json()
            print(f"Result: {result}")
        else:
            print(f"❌ API returned status {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Server might not be running")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_simple_api() 