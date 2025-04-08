from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Exercício')
    muscle_group = models.CharField(max_length=100, verbose_name='Grupo Muscular')
    notes = models.TextField(blank=True, null=True, verbose_name='Notas')

class Day(models.Model):
    date = models.DateField(verbose_name='Data')
    notes = models.TextField(blank=True, null=True, verbose_name='Notas')

    def __str__(self):
        return f'Sessão de Treino em {self.date}'
    
class WorkoutExercise(models.Model):
    workout_session = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='exercises', verbose_name='Sessão de Treino')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='workout_exercises', verbose_name='Exercício')
    weight = models.FloatField(verbose_name='Peso')
    reps = models.IntegerField(verbose_name='Repetições')
    set_number = models.IntegerField(verbose_name='Número da Série')