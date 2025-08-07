#!/usr/bin/env python3
"""
Script to check the feature requirements of the trained models.
"""

import joblib
import os

def check_model_features():
    """Check the feature requirements of the trained models."""
    print("🔍 Checking Model Feature Requirements")
    print("=" * 50)
    
    # Check Model 1
    model1_path = 'models/model1.pkl'
    if os.path.exists(model1_path):
        try:
            model1 = joblib.load(model1_path)
            print(f"✅ Model 1 loaded successfully")
            print(f"   Type: {type(model1).__name__}")
            if hasattr(model1, 'n_features_in_'):
                print(f"   Expected features: {model1.n_features_in_}")
            else:
                print(f"   Expected features: Unknown")
            
            # Check if it's a DecisionTreeClassifier
            if hasattr(model1, 'tree_'):
                print(f"   Tree structure: {model1.tree_.n_features}")
        except Exception as e:
            print(f"❌ Error loading Model 1: {e}")
    else:
        print(f"❌ Model 1 not found at {model1_path}")
    
    print()
    
    # Check Model 2
    model2_path = 'models/model2.pkl'
    if os.path.exists(model2_path):
        try:
            model2 = joblib.load(model2_path)
            print(f"✅ Model 2 loaded successfully")
            print(f"   Type: {type(model2).__name__}")
            if hasattr(model2, 'n_features_in_'):
                print(f"   Expected features: {model2.n_features_in_}")
            else:
                print(f"   Expected features: Unknown")
            
            # Check if it's a DecisionTreeClassifier
            if hasattr(model2, 'tree_'):
                print(f"   Tree structure: {model2.tree_.n_features}")
        except Exception as e:
            print(f"❌ Error loading Model 2: {e}")
    else:
        print(f"❌ Model 2 not found at {model2_path}")

if __name__ == "__main__":
    check_model_features() 