from rest_framework import viewsets
from .models import Exercise, Day, WorkoutExercise
from .serializers import ExerciseSerializer, DaySerializer, WorkoutExerciseSerializer

class ExerciseView(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class DayView(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class WorkoutExerciseView(viewsets.ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer