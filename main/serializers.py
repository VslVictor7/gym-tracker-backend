from rest_framework import serializers
from .models import Exercise, WorkoutSession, WorkoutExercise, WorkoutSet

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSet
        fields = '__all__'

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    sets = WorkoutSetSerializer(many=True, read_only=True, source='workoutset_set')

    class Meta:
        model = WorkoutExercise
        fields = '__all__'

class WorkoutSessionSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(many=True, read_only=True, source='workoutexercise_set')

    class Meta:
        model = WorkoutSession
        fields = '__all__'