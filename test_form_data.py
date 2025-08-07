#!/usr/bin/env python
"""
Test script to verify form data retrieval with teams in the dataset.
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_predictor.settings')
django.setup()

from analytics import get_team_recent_form
from data_loader import load_data

def test_form_data():
    """Test form data retrieval for teams in the dataset."""
    
    try:
        # Load data
        data1, data2 = load_data()
        print("✅ Data loaded successfully")
        
        # Test with teams that are in the dataset
        test_teams = ['Ajax', 'Feyenoord', 'PSV Eindhoven', 'Utrecht']
        
        for team in test_teams:
            try:
                form = get_team_recent_form(team, data1, version="v1")
                print(f"📊 {team}: {form}")
            except Exception as e:
                print(f"❌ Error getting form for {team}: {e}")
        
        # Test with teams not in dataset
        missing_teams = ['Grasshoppers', 'Winterthur', 'Leicester', 'Newcastle']
        
        print("\n--- Teams not in dataset (should show default form) ---")
        for team in missing_teams:
            try:
                form = get_team_recent_form(team, data1, version="v1")
                print(f"📊 {team}: {form}")
            except Exception as e:
                print(f"❌ Error getting form for {team}: {e}")
                
    except Exception as e:
        print(f"❌ Error loading data: {e}")

if __name__ == '__main__':
    print("Testing form data retrieval...")
    test_form_data() 