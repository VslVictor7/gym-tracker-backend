from django.urls import path
from .views import ExerciseViewSet, WorkoutSessionViewSet, WorkoutExerciseViewSet, WorkoutSetViewSet

urlpatterns = [
   path('exercicio/', ExerciseViewSet.as_view(), name='login'),
   path('p/', WorkoutExerciseViewSet.as_view(), name='post-list'),
   path('posts/<int:pk>/', WorkoutSessionViewSet.as_view(), name='post-detail'),
   path('posts/<int:pk>/comments/', WorkoutSetViewSet.as_view(), name='comment-list'),
]