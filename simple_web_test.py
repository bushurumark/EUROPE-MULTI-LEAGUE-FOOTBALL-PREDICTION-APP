#!/usr/bin/env python3
"""
Simple test to verify web interface historical probabilities
"""

def test_probability_format():
    """Test the probability format conversion for web interface"""
    
    print("🔍 Testing Web Interface Probability Format")
    print("=" * 40)
    
    # Simulate historical probabilities from the backend
    backend_probabilities = {
        "Home Team Win": 36.4,
        "Draw": 45.5,
        "Away Team Win": 18.2
    }
    
    print(f"✅ Backend probabilities: {backend_probabilities}")
    
    # Convert to web format
    web_probabilities = {}
    for outcome, prob in backend_probabilities.items():
        if outcome == "Home Team Win":
            web_probabilities['Home'] = prob
        elif outcome == "Draw":
            web_probabilities['Draw'] = prob
        elif outcome == "Away Team Win":
            web_probabilities['Away'] = prob
    
    print(f"✅ Web format probabilities: {web_probabilities}")
    
    # Convert to template format (decimal)
    template_probabilities = {}
    for outcome, prob in web_probabilities.items():
        template_probabilities[outcome] = prob / 100.0
    
    print(f"✅ Template format probabilities: {template_probabilities}")
    
    # Display expected web output
    print(f"\n🎯 Expected Web Display:")
    print("🤖 Prediction Probabilities:")
    for outcome, prob in web_probabilities.items():
        if outcome == "Home":
            print(f"  Home Win {prob:.1f}%")
        elif outcome == "Draw":
            print(f"  Draw {prob:.1f}%")
        elif outcome == "Away":
            print(f"  Away Win {prob:.1f}%")
    
    print("\n✅ Format conversion test completed!")

if __name__ == "__main__":
    test_probability_format() 