#!/usr/bin/env python3
"""
Minimal test to check Django setup
"""

import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_predictor.settings')

try:
    django.setup()
    print("✅ Django setup successful")
    
    # Test basic imports
    from django.http import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    print("✅ Django imports successful")
    
    # Test simple view function
    @csrf_exempt
    def test_view(request):
        return JsonResponse({'test': 'success'})
    
    print("✅ View function created successfully")
    print("✅ All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc() 