from django.db import models
from accounts.models import User

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Exercício')
    muscle_group = models.CharField(max_length=100, verbose_name='Grupo Muscular')
    notes = models.TextField(blank=True, null=True, verbose_name='Notas')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Exercício"
        verbose_name_plural = "Exercícios"

class Day(models.Model):
    date = models.DateField(verbose_name='Data')
    notes = models.TextField(blank=True, null=True, verbose_name='Notas')

    def __str__(self):
        return f'Sessão de Treino em {self.date}'
    
class Sessions(models.Model):
    workout_session = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='exercises', verbose_name='Sessão de Treino')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='workout_exercises', verbose_name='Exercício')
    weight = models.FloatField(verbose_name='Peso')
    reps = models.IntegerField(verbose_name='Repetições')
    set_number = models.IntegerField(verbose_name='Número da Série')

    def __str__(self):
        return f'{self.exercise.name} em {self.workout_session.date}'
    
    class Meta:
        verbose_name = "Exercício do Treino"
        verbose_name_plural = "Exercícios do Treino"
        
    
class PersonalWeight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="weight_entries")
    date = models.DateField()
    weight_morning = models.FloatField()
    weight_night = models.FloatField()

    def __str__(self):
        return f"{self.date} - Início: {self.weight_morning}kg / Final: {self.weight_night}kg"
    
    class Meta:
        verbose_name = "Peso Pessoal"
        verbose_name_plural = "Pesos Pessoais"