from django.contrib import admin
from django.contrib.admin.models import LogEntry
from user.models import Customer, Manager

LogEntry.__str__ = lambda self: str(self.object_repr)

admin.site.register(Customer)
admin.site.register(Manager)
