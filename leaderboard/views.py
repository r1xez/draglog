from django.shortcuts import render

from leaderboard.models import RecordLog

# Create your views here.
def leaderboard_view(request):
    records_0_100 = RecordLog.objects.filter(test_type='0-100').order_by('time_seconds')[:10]
    records_0_200 = RecordLog.objects.filter(test_type='0-200').order_by('time_seconds')[:10]
    records_100_200 = RecordLog.objects.filter(test_type='100-200').order_by('time_seconds')[:10]
    records_400m = RecordLog.objects.filter(test_type='400m').order_by('time_seconds')[:10]

    context = {
        'records_0_100': records_0_100,
        'records_0_200': records_0_200,
        'records_100_200': records_100_200,
        'records_400m': records_400m,
    }
    return render(request, 'leaderboard/leaderboard.html', context)