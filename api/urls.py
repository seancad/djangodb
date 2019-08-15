from django.urls import path, include
from .views import RentalViewSet
from rest_framework import routers

router =routers.DefaultRouter()
router.register('rentals',RentalViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]
