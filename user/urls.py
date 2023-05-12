from django.urls import path
from .views import CustomerCreateView, ManagerCreateView, AdminCreateView

urlpatterns = [
    path('customer/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('manager/create/', ManagerCreateView.as_view(), name='manager-create'),
    path('admin/create/', AdminCreateView.as_view(), name='admin-create'),
]
app_name = "user"
