#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Terminal-based Football Prediction App
A simplified version without Streamlit interface for testing in terminal
"""

import sys
import os
from data_loader import download_models, load_data
from controller import run_prediction
from leagues import leagues
import pandas as pd

def print_banner():
    """Print application banner"""
    print("=" * 60)
    print("⚽ FOOTBALL PREDICTION APP - TERMINAL VERSION")
    print("=" * 60)
    print()

def print_available_leagues():
    """Display available leagues and categories"""
    print("📋 Available Categories and Leagues:")
    print("-" * 40)
    for category, category_leagues in leagues.items():
        print(f"\n🏆 {category}:")
        for league in category_leagues.keys():
            print(f"  • {league}")
    print()

def get_user_input_terminal():
    """Get user input via terminal"""
    print("Please select your match details:")
    print("-" * 30)
    
    # Select category
    categories = list(leagues.keys())
    print("\nAvailable Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    cat_choice = int(input(f"\nSelect category (1-{len(categories)}): ")) - 1
    category = categories[cat_choice]
    
    # Select league
    category_leagues = list(leagues[category].keys())
    print(f"\nAvailable Leagues in {category}:")
    for i, league in enumerate(category_leagues, 1):
        print(f"{i}. {league}")
    
    league_choice = int(input(f"\nSelect league (1-{len(category_leagues)}): ")) - 1
    league = category_leagues[league_choice]
    
    # Select teams
    teams = leagues[category][league]
    print(f"\nAvailable Teams in {league}:")
    for i, team in enumerate(teams, 1):
        print(f"{i}. {team}")
    
    home_choice = int(input(f"\nSelect Home Team (1-{len(teams)}): ")) - 1
    home_team = teams[home_choice]
    
    away_choice = int(input(f"\nSelect Away Team (1-{len(teams)}): ")) - 1
    away_team = teams[away_choice]
    
    return category, league, home_team, away_team

def display_prediction_result(final, model_probs, hist_probs, home_form, away_form, h2h, home_team, away_team):
    """Display prediction results in terminal"""
    print("\n" + "=" * 60)
    print("🔮 PREDICTION RESULTS")
    print("=" * 60)
    
    # Final prediction
    print(f"\n🏆 Final Prediction: {final}")
    
    # Prediction probabilities (showing historical probabilities)
    if hist_probs:
        print(f"\n🤖 Prediction Probabilities:")
        for outcome, prob in hist_probs.items():
            if outcome == "Home Team Win":
                print(f"  Home Win {prob:.1f}%")
            elif outcome == "Draw":
                print(f"  Draw {prob:.1f}%")
            elif outcome == "Away Team Win":
                print(f"  Away Win {prob:.1f}%")
            else:
                print(f"  {outcome} {prob:.1f}%")
    
    # Model probabilities (for reference)
    if model_probs:
        print(f"\n📊 Model Probabilities:")
        for outcome, prob in model_probs.items():
            print(f"  • {outcome}: {prob * 100:.2f}%")
    
    # Recent form
    if home_form and away_form:
        print(f"\n📈 Recent Team Form (Last 5 Matches):")
        print(f"  • {home_team}: {home_form}")
        print(f"  • {away_team}: {away_form}")
    
    # Head-to-head history
    if h2h is not None and (not hasattr(h2h, 'empty') or not h2h.empty):
        print(f"\n🔁 Head-to-Head History:")
        result_col = 'FTR' if 'FTR' in h2h.columns else 'Res'
        result_map = {'H': 'Home Win', 'D': 'Draw', 'A': 'Away Win'}
        
        # Show last 5 matches
        recent_h2h = h2h.head(5)
        for _, match in recent_h2h.iterrows():
            result = result_map.get(match[result_col], match[result_col])
            date = match.get('Date', 'Unknown Date')
            print(f"  • {date}: {result}")
    
    print("\n" + "=" * 60)

def main():
    """Main application function"""
    print_banner()
    
    # Load models and data
    print("🔄 Loading models and data...")
    try:
        model1, model2 = download_models()
        data1, data2 = load_data()
        print("✅ Models and data loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading models/data: {e}")
        return
    
    print_available_leagues()
    
    while True:
        try:
            # Get user input
            category, league, home_team, away_team = get_user_input_terminal()
            
            print(f"\n🎯 Predicting: {home_team} vs {away_team} ({league})")
            print("Processing...")
            
            # Run prediction
            version = "v2" if category == "Others" else "v1"
            data = data2 if version == "v2" else data1
            model = model2 if version == "v2" else model1
            
            final, model_probs, hist_probs, home_form, away_form, h2h = run_prediction(
                home_team, away_team, model, data, version
            )
            
            if final is None:
                print("\n⚠️  Not enough historical data available for prediction.")
            else:
                display_prediction_result(final, model_probs, hist_probs, home_form, away_form, h2h, home_team, away_team)
            
            # Ask if user wants to continue
            print("\n" + "-" * 40)
            continue_choice = input("Would you like to make another prediction? (y/n): ").lower().strip()
            if continue_choice not in ['y', 'yes']:
                print("\n👋 Thank you for using Football Prediction App!")
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            retry = input("Would you like to try again? (y/n): ").lower().strip()
            if retry not in ['y', 'yes']:
                break

if __name__ == "__main__":
    main() 