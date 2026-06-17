from django.contrib import admin
from .models import RecordLog

@admin.register(RecordLog)
class RecordLogAdmin(admin.ModelAdmin):
    
    list_display = ('user_car', 'test_type', 'time_seconds', 'date_added')
    
    
    list_filter = ('test_type', 'date_added')
    
    
    search_fields = ('user_car__user__username', 'user_car__car_base__name')