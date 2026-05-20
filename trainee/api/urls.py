from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TraineeViewSet

router=DefaultRouter()
router.register('trainees',TraineeViewSet,basename='trainees')

urlpatterns=[
    path('',include(router.urls)),
]