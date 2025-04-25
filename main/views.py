from rest_framework import viewsets, permissions
from .models import Exercise, Day, WorkoutExercise
from .serializers import *

class ExerciseView(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class DayView(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class WorkoutExerciseView(viewsets.ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer

class WeightEntryView(viewsets.ModelViewSet):
    serializer_class = WeightEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PersonalWeight.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)