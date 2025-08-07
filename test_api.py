#!/usr/bin/env python3
"""
Test script for the API endpoint
"""

import requests
import json

def test_api_endpoint():
    """Test the API endpoint with a POST request"""
    
    # Test data
    data = {
        'home_team': 'Man City',
        'away_team': 'Liverpool',
        'category': 'Premier League'
    }
    
    # Make POST request to the API endpoint
    url = 'http://localhost:8000/api/predict/'
    
    # Test with different content types
    headers_list = [
        {'Content-Type': 'application/x-www-form-urlencoded'},
        {'Content-Type': 'application/json'},
        {}  # No content type
    ]
    
    for i, headers in enumerate(headers_list):
        print(f"\n--- Test {i+1}: {headers} ---")
        try:
            if headers.get('Content-Type') == 'application/json':
                response = requests.post(url, json=data, headers=headers)
            else:
                response = requests.post(url, data=data, headers=headers)
            
            print(f"Status Code: {response.status_code}")
            print(f"Response Content: {response.text}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Success! Result: {json.dumps(result, indent=2)}")
                return
            else:
                print(f"❌ Error: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection Error: Make sure the Django server is running on localhost:8000")
        except Exception as e:
            print(f"❌ Error: {e}")

def test_get_request():
    """Test what happens with a GET request"""
    url = 'http://localhost:8000/api/predict/'
    
    try:
        response = requests.get(url)
        print(f"\n--- GET Request Test ---")
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Testing API endpoint...")
    test_api_endpoint()
    test_get_request() 