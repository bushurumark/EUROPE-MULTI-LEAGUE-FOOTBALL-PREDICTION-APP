#!/usr/bin/env python3
"""
Test script to check if all imports work correctly
"""

import sys
import os

def test_imports():
    """Test all the imports used in views.py"""
    
    print("Testing imports...")
    
    try:
        # Test basic imports
        import pickle
        import joblib
        import pandas as pd
        import numpy as np
        import warnings
        print("✅ Basic imports successful")
        
        # Test Django imports
        from django.shortcuts import render, redirect
        from django.contrib.auth.decorators import login_required
        from django.contrib import messages
        from django.http import JsonResponse
        from django.views.decorators.csrf import csrf_exempt
        print("✅ Django imports successful")
        
        # Test local imports
        from predictor.models import Prediction, Match, Team
        print("✅ Django model imports successful")
        
        # Test analytics imports
        from predictor.analytics import preprocess_for_model1, advanced_predict_match
        print("✅ Analytics imports successful")
        
        # Test other local imports
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        
        from data_loader import download_models, load_data
        print("✅ Data loader imports successful")
        
        from model_utils import (
            align_features,
            compute_mean_for_teams,
            calculate_probabilities,
            predict_with_confidence,
            determine_final_prediction
        )
        print("✅ Model utils imports successful")
        
        from controller import run_prediction
        print("✅ Controller imports successful")
        
        from analytics import (
            get_column_names,
            get_team_recent_form,
            get_head_to_head_history
        )
        print("✅ Analytics function imports successful")
        
        from leagues import leagues
        print("✅ Leagues imports successful")
        
        print("🎉 All imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_imports() 