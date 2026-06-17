from django.shortcuts import render
from .models import RecordLog
from garage.models import Brand

def leaderboard_view(request):
    """Global leaderboard with advanced filtering."""
    
    queryset = RecordLog.objects.select_related('user_car__user', 'user_car__car_base__brand').all()

    
    test_type = request.GET.get('test_type', '0-100')
    queryset = queryset.filter(test_type=test_type)

    
    brand_id = request.GET.get('brand')
    if brand_id:
        queryset = queryset.filter(user_car__car_base__brand_id=brand_id)

   
    fuel_type = request.GET.get('fuel_type')
    if fuel_type:
        queryset = queryset.filter(user_car__fuel_type=fuel_type)

   
    stage = request.GET.get('stage')
    if stage:
        queryset = queryset.filter(user_car__stage=stage)

  
    records = queryset.order_by('time_seconds')[:50]

    
    context = {
        'records': records,
        'brands': Brand.objects.all(),
        'test_types': RecordLog.TYPE_CHOICES,
        'fuel_choices': [choice[0] for choice in [('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')]],
        'stage_choices': [choice[0] for choice in [('Stock', 'Stock'), ('Stage 1', 'Stage 1'), ('Stage 2', 'Stage 2'), ('Stage 3', 'Stage 3'), ('Stage 4', 'Stage 4')]],
       
        'current_filters': request.GET,
    }
    return render(request, 'leaderboard/leaderboard.html', context)