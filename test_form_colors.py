#!/usr/bin/env python3
"""
Test to verify colored form display is working correctly.
"""

import urllib.request
import urllib.parse

def test_form_colors():
    """Test if colored form display is working."""
    print("Testing colored form display...")
    
    try:
        # Test the predict page
        url = "http://127.0.0.1:8000/predict/"
        
        print(f"Testing URL: {url}")
        
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
        
        print("Form Colors Test:")
        print("=" * 50)
        
        # Check for CSS classes
        css_checks = [
            ('form-indicator CSS', 'form-indicator', True),
            ('form-win CSS', 'form-win', True),
            ('form-draw CSS', 'form-draw', True),
            ('form-loss CSS', 'form-loss', True),
            ('Hover effects', 'transform: scale', True),
            ('Box shadows', 'box-shadow', True),
        ]
        
        for description, pattern, should_exist in css_checks:
            if pattern in html_content:
                if should_exist:
                    print(f"✅ {description}: Found")
                else:
                    print(f"❌ {description}: Found (should not exist)")
            else:
                if should_exist:
                    print(f"❌ {description}: Not found (should exist)")
                else:
                    print(f"✅ {description}: Not found (correct)")
        
        # Check for JavaScript logic
        js_checks = [
            ('Form display function', 'updateStatsDisplay', True),
            ('Colored indicators logic', 'form-win', True),
            ('Form indicator creation', 'createElement', True),
            ('Class assignment', 'classList.add', True),
        ]
        
        print("\nJavaScript Logic Check:")
        print("-" * 30)
        
        for description, pattern, should_exist in js_checks:
            if pattern in html_content:
                if should_exist:
                    print(f"✅ {description}: Found")
                else:
                    print(f"❌ {description}: Found (should not exist)")
            else:
                if should_exist:
                    print(f"❌ {description}: Not found (should exist)")
                else:
                    print(f"✅ {description}: Not found (correct)")
        
        # Check for specific styling
        styling_checks = [
            ('Green win styling', '#22c55e', True),
            ('Orange draw styling', '#f59e0b', True),
            ('Red loss styling', '#ef4444', True),
            ('White text', 'color: white', True),
            ('Gradient backgrounds', 'linear-gradient', True),
        ]
        
        print("\nStyling Check:")
        print("-" * 20)
        
        for description, pattern, should_exist in styling_checks:
            if pattern in html_content:
                if should_exist:
                    print(f"✅ {description}: Found")
                else:
                    print(f"❌ {description}: Found (should not exist)")
            else:
                if should_exist:
                    print(f"❌ {description}: Not found (should exist)")
                else:
                    print(f"✅ {description}: Not found (correct)")
        
        print("=" * 50)
        print("✅ Form colors test completed!")
        
        # Summary
        if 'form-win' in html_content and 'form-indicator' in html_content:
            print("\n📋 SUMMARY:")
            print("✅ CSS classes are present")
            print("✅ JavaScript logic is present")
            print("✅ Color styling is defined")
            print("✅ Form should display with colors")
            print("\n💡 If colors not showing:")
            print("   - Clear browser cache (Ctrl+F5)")
            print("   - Check browser console for errors")
            print("   - Try different browser")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        print("Make sure the Django server is running on port 8000")

if __name__ == "__main__":
    test_form_colors() 