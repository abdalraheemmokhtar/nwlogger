# request_logger/admin.py
from django.contrib import admin
from .models import RequestLog

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'request_path', 'http_method', 'timestamp')
    list_filter = ('http_method', 'timestamp')
    search_fields = ('ip_address', 'user_agent', 'request_path')
    date_hierarchy = 'timestamp'
