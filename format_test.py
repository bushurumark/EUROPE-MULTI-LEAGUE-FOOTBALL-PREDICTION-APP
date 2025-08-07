#!/usr/bin/env python3
"""
Test to verify the exact format for prediction probabilities
"""

def test_exact_format():
    """Test the exact format you want"""
    
    print("🔍 Testing Exact Format")
    print("=" * 30)
    
    # The format you want
    print("\n🤖 Prediction Probabilities:")
    print("  Home Win 33.3%")
    print("  Draw 33.4%")
    print("  Away Win 33.3%")
    
    # Test with actual data
    hist_probs = {
        "Home Team Win": 33.3,
        "Draw": 33.4,
        "Away Team Win": 33.3
    }
    
    print("\n🤖 Prediction Probabilities (from data):")
    for outcome, prob in hist_probs.items():
        if outcome == "Home Team Win":
            print(f"  Home Win {prob:.1f}%")
        elif outcome == "Draw":
            print(f"  Draw {prob:.1f}%")
        elif outcome == "Away Team Win":
            print(f"  Away Win {prob:.1f}%")
        else:
            print(f"  {outcome} {prob:.1f}%")
    
    print("\n✅ Format test completed!")

if __name__ == "__main__":
    test_exact_format() 