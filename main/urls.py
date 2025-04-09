from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from .views import (
    ExerciseView, DayView, WorkoutExerciseView,
)

router = DefaultRouter()

router.register('exercise', ExerciseView, basename='exercise')
router.register('day', DayView, basename='day')
router.register('workout-session', WorkoutExerciseView, basename='workout-session')

urlpatterns = [
    path('', include(router.urls)),
]