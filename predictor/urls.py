from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'predictor'

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('result/', views.result, name='result'),
    path('history/', views.history, name='history'),
    path('about/', views.about, name='about'),
    path('api/predict/', views.api_predict, name='api_predict'),
    path('api/predict-simple/', views.api_predict_simple, name='api_predict_simple'),
    path('api/find-team/', views.api_find_team, name='api_find_team'),
    path('api/teams/', views.get_teams_by_category, name='get_teams_by_category'),
    path('api/team-stats/', views.api_team_stats, name='api_team_stats'),
    path('api/head-to-head/', views.api_head_to_head, name='api_head_to_head'),
    path('api/market-odds/', views.api_market_odds, name='api_market_odds'),
    path('api/historical-probabilities/', views.api_historical_probabilities, name='api_historical_probabilities'),
    path('historical-probabilities/', views.historical_probabilities, name='historical_probabilities'),
    # Service worker route
    path('sw.js', views.service_worker, name='service_worker'),
]
