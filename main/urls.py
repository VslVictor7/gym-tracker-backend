from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from .views import *

router = DefaultRouter()

router.register('exercises', ExerciseView, basename='exercises')
router.register('days', DayView, basename='days')
router.register('workout-sessions', SessionsView, basename='workout-sessions')
router.register('body-weight', WeightEntryView, basename='body-weight')

urlpatterns = [
    path('', include(router.urls)),
]