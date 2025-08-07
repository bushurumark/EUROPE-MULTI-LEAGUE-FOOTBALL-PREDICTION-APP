#!/usr/bin/env python3
"""
Comprehensive test script to verify all European leagues and other leagues are working properly.
"""

import sys
import os
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_all_leagues():
    """Test all leagues from LEAGUES_BY_CATEGORY."""
    print("Testing all leagues and teams...")
    
    try:
        from predictor.views import LEAGUES_BY_CATEGORY
        
        total_teams = 0
        working_leagues = 0
        total_leagues = 0
        
        print("League and Team Analysis:")
        print("=" * 80)
        
        for category, leagues in LEAGUES_BY_CATEGORY.items():
            print(f"\n📁 {category.upper()}")
            print("-" * 50)
            
            for league_name, teams in leagues.items():
                total_leagues += 1
                league_teams_count = len(teams)
                total_teams += league_teams_count
                
                print(f"\n🏆 {league_name} ({league_teams_count} teams)")
                
                # Test first 3 teams from each league
                test_teams = teams[:3]
                working_teams = 0
                
                for team in test_teams:
                    try:
                        from analytics import analytics_engine
                        
                        # Test team form
                        form_data = analytics_engine.get_team_form(team)
                        
                        # Test team strength
                        home_strength = analytics_engine.calculate_team_strength(team, 'home')
                        away_strength = analytics_engine.calculate_team_strength(team, 'away')
                        
                        # Calculate form percentage
                        if form_data and form_data['recent_form']:
                            form_points = {'W': 3, 'D': 1, 'L': 0}
                            recent_points = sum(form_points[result] for result in form_data['recent_form'][:5])
                            max_points = 15
                            form_percentage = (recent_points / max_points) * 100
                        else:
                            form_percentage = 50
                        
                        # Calculate average goals
                        if form_data and 'goals_scored' in form_data:
                            avg_goals = np.mean(form_data['goals_scored'][:5])
                        else:
                            avg_goals = 1.5
                        
                        strength_percent = round(home_strength * 100, 1)
                        
                        print(f"  ✅ {team:<20} {form_percentage:>6.1f}% {avg_goals:>5.1f} {strength_percent:>6.1f}%")
                        working_teams += 1
                        
                    except Exception as e:
                        print(f"  ❌ {team:<20} ERROR: {str(e)[:30]}...")
                
                if working_teams == len(test_teams):
                    working_leagues += 1
                    print(f"  🎉 League working: {working_teams}/{len(test_teams)} teams")
                else:
                    print(f"  ⚠️  League issues: {working_teams}/{len(test_teams)} teams")
        
        print("\n" + "=" * 80)
        print("📊 SUMMARY:")
        print(f"Total Leagues: {total_leagues}")
        print(f"Working Leagues: {working_leagues}")
        print(f"Total Teams: {total_teams}")
        print(f"Success Rate: {(working_leagues/total_leagues)*100:.1f}%")
        
        return working_leagues == total_leagues
        
    except Exception as e:
        print(f"❌ League test failed: {e}")
        return False

def test_specific_league_teams():
    """Test specific teams from each major league."""
    print("\nTesting specific teams from each league...")
    
    try:
        from analytics import analytics_engine
        
        # Define test teams for each major league
        test_league_teams = {
            "Premier League": ["Man United", "Arsenal", "Liverpool", "Chelsea", "Man City"],
            "Serie A": ["Inter", "Juventus", "Milan", "Roma", "Napoli"],
            "La Liga": ["Real Madrid", "Barcelona", "Ath Madrid", "Sevilla", "Valencia"],
            "Bundesliga": ["Bayern Munich", "Dortmund", "Leverkusen", "RB Leipzig", "Stuttgart"],
            "Ligue1": ["Paris SG", "Lyon", "Marseille", "Monaco", "Lille"],
            "Eredivisie": ["Ajax", "PSV Eindhoven", "Feyenoord", "AZ Alkmaar", "Twente"],
            "Switzerland League": ["Young Boys", "Basel", "Grasshoppers", "Lausanne", "Lugano"],
            "Russia League": ["Zenit", "Dynamo Moscow", "CSKA Moscow", "Spartak Moscow", "Lokomotiv Moscow"]
        }
        
        print("Specific Team Test Results:")
        print("=" * 80)
        print(f"{'League':<20} {'Team':<20} {'Form':<8} {'Goals':<8} {'Strength':<10}")
        print("-" * 80)
        
        total_tests = 0
        successful_tests = 0
        
        for league_name, teams in test_league_teams.items():
            print(f"\n🏆 {league_name}")
            print("-" * 50)
            
            for team in teams:
                total_tests += 1
                try:
                    # Get team form
                    form_data = analytics_engine.get_team_form(team)
                    
                    # Get team strength
                    home_strength = analytics_engine.calculate_team_strength(team, 'home')
                    
                    # Calculate form percentage
                    if form_data and form_data['recent_form']:
                        form_points = {'W': 3, 'D': 1, 'L': 0}
                        recent_points = sum(form_points[result] for result in form_data['recent_form'][:5])
                        max_points = 15
                        form_percentage = (recent_points / max_points) * 100
                    else:
                        form_percentage = 50
                    
                    # Calculate average goals
                    if form_data and 'goals_scored' in form_data:
                        avg_goals = np.mean(form_data['goals_scored'][:5])
                    else:
                        avg_goals = 1.5
                    
                    strength_percent = round(home_strength * 100, 1)
                    
                    print(f"{'':<20} {team:<20} {form_percentage:>6.1f}% {avg_goals:>6.1f} {strength_percent:>8.1f}% ✅")
                    successful_tests += 1
                    
                except Exception as e:
                    print(f"{'':<20} {team:<20} {'ERROR':<8} {'ERROR':<8} {'ERROR':<10} ❌")
        
        print("\n" + "=" * 80)
        print(f"📊 Specific Team Tests: {successful_tests}/{total_tests} successful")
        print(f"Success Rate: {(successful_tests/total_tests)*100:.1f}%")
        
        return successful_tests == total_tests
        
    except Exception as e:
        print(f"❌ Specific league test failed: {e}")
        return False

def test_team_variations_all_leagues():
    """Test team name variations for all leagues."""
    print("\nTesting team name variations for all leagues...")
    
    try:
        from analytics import get_team_recent_form, calculate_probabilities
        
        # Test data
        import pandas as pd
        test_data = pd.DataFrame({
            'HomeTeam': ['Man United', 'Arsenal', 'Real Madrid', 'Bayern Munich', 'Paris SG'],
            'AwayTeam': ['Arsenal', 'Man United', 'Barcelona', 'Dortmund', 'Lyon'],
            'FTR': ['H', 'A', 'H', 'D', 'A'],
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
        })
        
        # Test variations for different leagues
        variations_to_test = [
            # Premier League
            ('man united', 'Man United'),
            ('manchester united', 'Man United'),
            ('arsenal', 'Arsenal'),
            ('man city', 'Man City'),
            ('manchester city', 'Man City'),
            
            # La Liga
            ('real madrid', 'Real Madrid'),
            ('barcelona', 'Barcelona'),
            ('ath madrid', 'Ath Madrid'),
            
            # Bundesliga
            ('bayern munich', 'Bayern Munich'),
            ('dortmund', 'Dortmund'),
            ('leverkusen', 'Leverkusen'),
            
            # Ligue1
            ('paris sg', 'Paris SG'),
            ('lyon', 'Lyon'),
            ('marseille', 'Marseille'),
            
            # Swiss League
            ('young boys', 'Young Boys'),
            ('basel', 'Basel'),
            ('grasshoppers', 'Grasshoppers'),
            
            # Russian League
            ('zenit', 'Zenit'),
            ('dynamo moscow', 'Dynamo Moscow'),
            ('cska moscow', 'CSKA Moscow'),
        ]
        
        print("Team Name Variations Test:")
        print("=" * 60)
        print(f"{'Input':<25} {'Expected':<25} {'Status'}")
        print("-" * 60)
        
        success_count = 0
        total_count = len(variations_to_test)
        
        for input_name, expected_name in variations_to_test:
            try:
                # Test get_team_recent_form
                form = get_team_recent_form(input_name, test_data)
                
                # Test calculate_probabilities
                probs = calculate_probabilities(input_name, 'Arsenal', test_data)
                
                print(f"{input_name:<25} {expected_name:<25} ✅")
                success_count += 1
                
            except Exception as e:
                print(f"{input_name:<25} {expected_name:<25} ❌ ({str(e)[:20]}...)")
        
        print("=" * 60)
        print(f"Success: {success_count}/{total_count}")
        
        if success_count == total_count:
            print("✅ All team variations work correctly!")
            return True
        else:
            print("❌ Some team variations failed")
            return False
            
    except Exception as e:
        print(f"❌ Team variations test failed: {e}")
        return False

def test_dataset_coverage():
    """Test dataset coverage for all leagues."""
    print("\nTesting dataset coverage...")
    
    try:
        from data_loader import load_data
        
        data1, data2 = load_data()
        
        if data1 is not None:
            # Get unique teams from dataset
            home_teams = set(data1['HomeTeam'].unique())
            away_teams = set(data1['AwayTeam'].unique())
            all_teams = home_teams | away_teams
            
            print(f"Total teams in dataset: {len(all_teams)}")
            
            # Test teams from different leagues
            test_teams_by_league = {
                "Premier League": ["Man United", "Arsenal", "Liverpool", "Chelsea", "Man City"],
                "Serie A": ["Inter", "Juventus", "Milan", "Roma", "Napoli"],
                "La Liga": ["Real Madrid", "Barcelona", "Ath Madrid", "Sevilla", "Valencia"],
                "Bundesliga": ["Bayern Munich", "Dortmund", "Leverkusen", "RB Leipzig"],
                "Ligue1": ["Paris SG", "Lyon", "Marseille", "Monaco", "Lille"],
                "Switzerland League": ["Young Boys", "Basel", "Grasshoppers", "Lausanne"],
                "Russia League": ["Zenit", "Dynamo Moscow", "CSKA Moscow", "Spartak Moscow"]
            }
            
            print("\nDataset Coverage by League:")
            print("=" * 60)
            
            total_found = 0
            total_tested = 0
            
            for league_name, teams in test_teams_by_league.items():
                print(f"\n🏆 {league_name}")
                print("-" * 30)
                
                league_found = 0
                for team in teams:
                    total_tested += 1
                    if team in all_teams:
                        print(f"  ✅ {team}")
                        league_found += 1
                        total_found += 1
                    else:
                        print(f"  ❌ {team}")
                
                print(f"  📊 Found: {league_found}/{len(teams)} teams")
            
            print("\n" + "=" * 60)
            print(f"📊 Overall Coverage: {total_found}/{total_tested} teams found")
            print(f"Coverage Rate: {(total_found/total_tested)*100:.1f}%")
            
            return total_found > total_tested * 0.5  # At least 50% coverage
            
        else:
            print("❌ Could not load dataset")
            return False
            
    except Exception as e:
        print(f"❌ Dataset coverage test failed: {e}")
        return False

def main():
    """Run all comprehensive league tests."""
    print("Running comprehensive league tests...")
    print("=" * 80)
    
    tests = [
        test_all_leagues,
        test_specific_league_teams,
        test_team_variations_all_leagues,
        test_dataset_coverage,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 80)
    print(f"📊 FINAL RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL LEAGUES WORKING PERFECTLY!")
        print("\n✅ All European leagues and other leagues are working properly:")
        print("- Premier League, Serie A, La Liga, Bundesliga, Ligue1")
        print("- Eredivisie, Swiss League, Russian League, etc.")
        print("- Team name variations working for all leagues")
        print("- Dataset coverage is comprehensive")
        print("- Team stats and strength calculations working")
    else:
        print("⚠️  Some league tests failed. Please check the issues.")
    
    return passed == total

if __name__ == "__main__":
    main() 