from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import CustomerCreateView, ManagerCreateView, AdminCreateView

urlpatterns = [
    path("customer/create/", CustomerCreateView.as_view(), name="customer-create"),
    path("manager/create/", ManagerCreateView.as_view(), name="manager-create"),
    path("admin/create/", AdminCreateView.as_view(), name="admin-create"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
app_name = "user"
