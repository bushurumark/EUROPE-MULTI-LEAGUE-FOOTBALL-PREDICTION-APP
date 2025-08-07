#!/usr/bin/env python3
"""
Debug script to check what the API is actually returning.
"""

import sys
import os
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_predictor.settings')
django.setup()

def debug_api_response():
    """Debug the API response directly."""
    print("Debugging API response...")
    
    try:
        from predictor.views import api_team_stats
        from django.http import HttpRequest
        
        # Create a mock request
        request = HttpRequest()
        request.method = 'GET'
        request.GET = {'team': 'Man United'}
        
        # Call the API function directly
        from django.http import JsonResponse
        response = api_team_stats(request)
        
        if isinstance(response, JsonResponse):
            data = response.content.decode('utf-8')
            import json
            parsed_data = json.loads(data)
            
            print("API Response Data:")
            print(json.dumps(parsed_data, indent=2))
            
            # Check strength data specifically
            home_strength = parsed_data.get('home_strength')
            away_strength = parsed_data.get('away_strength')
            
            print(f"\nStrength Data:")
            print(f"Home Strength: {home_strength} (type: {type(home_strength)})")
            print(f"Away Strength: {away_strength} (type: {type(away_strength)})")
            
            if home_strength and away_strength:
                if home_strength != 77.0 and away_strength != 77.0:
                    print("✅ Varied strength values (not 77%)")
                else:
                    print("❌ Still showing 77% strength")
            else:
                print("❌ No strength data found")
                
        else:
            print(f"Unexpected response type: {type(response)}")
            
    except Exception as e:
        print(f"❌ Debug failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_api_response() 