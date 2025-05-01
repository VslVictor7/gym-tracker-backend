from rest_framework import serializers
from .models import *

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

class SessionsSerializer(serializers.ModelSerializer):
    exercise_name = serializers.SerializerMethodField()
    workout_date = serializers.SerializerMethodField()

    class Meta:
        model = Sessions
        fields = ['id', 'exercise_name', 'workout_date', 'weight', 'reps', 'set_number']

    def get_exercise_name(self, obj):
        return obj.exercise.name

    def get_workout_date(self, obj):
        return obj.workout_session.date
    
class WeightEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalWeight
        fields = '__all__'