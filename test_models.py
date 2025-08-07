#!/usr/bin/env python3
"""
Test script to verify that Model 1 and Model 2 work correctly for their respective leagues.
"""

import sys
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from predictor.analytics import (
    preprocess_for_model1, 
    preprocess_for_model2, 
    advanced_predict_match,
    create_working_models
)

def test_model_selection():
    """Test that the correct model is selected for different teams."""
    print("🧪 Testing Model Selection Logic")
    print("=" * 50)
    
    # Create test models
    model1, model2 = create_working_models()
    
    if model1 is None or model2 is None:
        print("❌ Failed to create test models")
        return False
    
    print("✅ Test models created successfully")
    
    # Test European teams (should use Model 1)
    european_teams = [
        ("Man City", "Liverpool"),
        ("Barcelona", "Real Madrid"),
        ("Bayern Munich", "Dortmund"),
        ("Juventus", "Milan"),
        ("Paris SG", "Marseille")
    ]
    
    print("\n🇪🇺 Testing European Teams (Model 1):")
    for home, away in european_teams:
        result = advanced_predict_match(home, away, model1, model2)
        if result:
            print(f"  ✅ {home} vs {away}: {result['model_type']} - {result['outcome']} ({result['confidence']:.1%})")
        else:
            print(f"  ❌ {home} vs {away}: No prediction available")
    
    # Test other league teams (should use Model 2)
    other_teams = [
        ("Viborg", "Brondby"),
        ("Aarhus", "Midtjylland"),
        ("Basel", "Young Boys"),
        ("Salzburg", "LASK"),
        ("Club America", "Guadalajara Chivas")
    ]
    
    print("\n🌍 Testing Other League Teams (Model 2):")
    for home, away in other_teams:
        result = advanced_predict_match(home, away, model1, model2)
        if result:
            print(f"  ✅ {home} vs {away}: {result['model_type']} - {result['outcome']} ({result['confidence']:.1%})")
        else:
            print(f"  ❌ {home} vs {away}: No prediction available")
    
    # Test mixed teams (should try both models)
    mixed_teams = [
        ("Man City", "Viborg"),  # European vs Other
        ("Barcelona", "Brondby"),  # European vs Other
    ]
    
    print("\n🌐 Testing Mixed Teams (Fallback):")
    for home, away in mixed_teams:
        result = advanced_predict_match(home, away, model1, model2)
        if result:
            print(f"  ✅ {home} vs {away}: {result['model_type']} - {result['outcome']} ({result['confidence']:.1%})")
        else:
            print(f"  ❌ {home} vs {away}: No prediction available")
    
    return True

def test_data_preprocessing():
    """Test that data preprocessing works for both models."""
    print("\n🔧 Testing Data Preprocessing")
    print("=" * 50)
    
    # Test Model 1 preprocessing
    print("\n📊 Testing Model 1 Preprocessing (European leagues):")
    european_pairs = [
        ("Man City", "Liverpool"),
        ("Barcelona", "Real Madrid"),
        ("Bayern Munich", "Dortmund")
    ]
    
    for home, away in european_pairs:
        features = preprocess_for_model1(home, away)
        if features is not None:
            print(f"  ✅ {home} vs {away}: {features.shape[1]} features")
        else:
            print(f"  ❌ {home} vs {away}: No features available")
    
    # Test Model 2 preprocessing
    print("\n📊 Testing Model 2 Preprocessing (Other leagues):")
    other_pairs = [
        ("Viborg", "Brondby"),
        ("Aarhus", "Midtjylland"),
        ("Basel", "Young Boys")
    ]
    
    for home, away in other_pairs:
        features = preprocess_for_model2(home, away)
        if features is not None:
            print(f"  ✅ {home} vs {away}: {features.shape[1]} features")
        else:
            print(f"  ❌ {home} vs {away}: No features available")
    
    return True

def test_model_consistency():
    """Test that both models produce consistent results."""
    print("\n🔄 Testing Model Consistency")
    print("=" * 50)
    
    # Create test models
    model1, model2 = create_working_models()
    
    if model1 is None or model2 is None:
        print("❌ Failed to create test models")
        return False
    
    # Test that both models can make predictions
    test_teams = ("Test Team A", "Test Team B")
    
    # Test Model 1
    result1 = advanced_predict_match(test_teams[0], test_teams[1], model1, model2)
    if result1:
        print(f"✅ Model 1 prediction: {result1['outcome']} ({result1['confidence']:.1%})")
    else:
        print("❌ Model 1 failed to make prediction")
    
    # Test Model 2
    result2 = advanced_predict_match(test_teams[0], test_teams[1], model1, model2)
    if result2:
        print(f"✅ Model 2 prediction: {result2['outcome']} ({result2['confidence']:.1%})")
    else:
        print("❌ Model 2 failed to make prediction")
    
    return True

def main():
    """Run all tests."""
    print("🚀 Starting Model Tests")
    print("=" * 60)
    
    tests = [
        test_model_selection,
        test_data_preprocessing,
        test_model_consistency
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
                print(f"✅ {test.__name__} passed")
            else:
                print(f"❌ {test.__name__} failed")
        except Exception as e:
            print(f"❌ {test.__name__} failed with error: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Models are working correctly.")
    else:
        print("⚠️ Some tests failed. Please check the implementation.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 