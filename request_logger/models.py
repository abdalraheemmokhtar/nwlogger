# request_logger/models.py
from django.db import models

class RequestLog(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    request_path = models.CharField(max_length=255)
    http_method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.ip_address} on {self.timestamp}"
