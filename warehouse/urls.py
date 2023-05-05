from django.urls import path, include
from rest_framework import routers

from warehouse.views import WarehouseItemViewSet

router = routers.DefaultRouter()
router.register("warehouse_items", WarehouseItemViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "warehouse"
