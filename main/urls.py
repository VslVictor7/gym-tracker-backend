from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from .views import (
    ExerciseView, DayView, WorkoutExerciseView,
)

router = DefaultRouter()

router.register('exercises', ExerciseView, basename='exercises')
router.register('days', DayView, basename='days')
router.register('workout-sessions', WorkoutExerciseView, basename='workout-sessions')

urlpatterns = [
    path('', include(router.urls)),
]