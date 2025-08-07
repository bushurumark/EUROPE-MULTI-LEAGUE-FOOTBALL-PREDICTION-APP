import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_predict_simple(request):
    """Simplified API endpoint for testing"""
    print(f"🔍 API Request Method: {request.method}")
    print(f"🔍 API Request Content Type: {request.content_type}")
    
    if request.method != 'POST':
        return JsonResponse({
            'error': 'Only POST requests are allowed'
        }, status=405)
    
    try:
        # Handle both JSON and form-data
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            # Handle form-data
            data = request.POST.dict()
        
        home_team = data.get('home_team')
        away_team = data.get('away_team')
        category = data.get('category', 'Unknown')
        
        print(f"🔍 Received API data: {data}")
        
        if not home_team or not home_team.strip():
            return JsonResponse({
                'error': 'Home team is required',
                'insufficient_data': True
            }, status=400)
        elif not away_team or not away_team.strip():
            return JsonResponse({
                'error': 'Away team is required',
                'insufficient_data': True
            }, status=400)
        elif home_team.strip() == away_team.strip():
            return JsonResponse({
                'error': 'Home and away teams cannot be the same',
                'insufficient_data': True
            }, status=400)
        
        # Return a simple test response
        return JsonResponse({
            'home_team': home_team,
            'away_team': away_team,
            'category': category,
            'home_score': 2,
            'away_score': 1,
            'outcome': 'Home Team Win',
            'prediction_number': 1,
            'confidence': 75.0,
            'message': 'Test prediction successful'
        })
        
    except Exception as e:
        print(f"❌ Error in API: {e}")
        return JsonResponse({
            'error': f'Internal server error: {str(e)}'
        }, status=500)

def home_simple(request):
    """Simplified home page"""
    return render(request, 'predictor/home.html', {
        'total_predictions': 0,
        'accuracy_rate': 75,
        'teams_covered': 500,
        'leagues_supported': 25,
        'recent_predictions': []
    }) 