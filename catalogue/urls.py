from django.urls import path, include
from rest_framework import routers

from catalogue.views import BrandViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register("bands", BrandViewSet)
router.register("products", ProductViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "catalogue"
