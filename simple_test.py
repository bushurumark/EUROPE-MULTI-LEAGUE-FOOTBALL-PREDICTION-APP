#!/usr/bin/env python3
"""
Simple test to verify prediction probabilities display format
"""

def test_display_format():
    """Test the display format for prediction probabilities"""
    
    print("🔍 Testing Display Format")
    print("=" * 30)
    
    # Simulate historical probabilities
    hist_probs = {
        "Home Team Win": 33.3,
        "Draw": 33.4,
        "Away Team Win": 33.3
    }
    
    print("\n🤖 Prediction Probabilities:")
    for outcome, prob in hist_probs.items():
        if outcome == "Home Team Win":
            print(f"  Home Win {prob:.1f}%")
        elif outcome == "Draw":
            print(f"  Draw {prob:.1f}%")
        elif outcome == "Away Team Win":
            print(f"  Away Win {prob:.1f}%")
        else:
            print(f"  {outcome} {prob:.1f}%")
    
    print("\n✅ Display format test completed!")

if __name__ == "__main__":
    test_display_format() 