
from django.db import models
from datetime import datetime, timedelta

class Positivity(models.Model):
    """Displaying the daily planners"""
    quote = models.TextField()
    affirmation = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'positivities'

    def __str__(self):
        return self.quote

class Reminder(models.Model):
    dailyplanner = models.ForeignKey(Positivity, on_delete=models.CASCADE)
    reminder = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.reminder
    
class Priority(models.Model):
    dailyplanner = models.ForeignKey(Positivity, on_delete=models.CASCADE)
    priority = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'priorities'

    def __str__(self):
        return self.priority
    
class ToDo(models.Model):
    dailyplanner = models.ForeignKey(Positivity, on_delete=models.CASCADE)
    todo = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo
    
class ExerciseType(models.Model):
    dailyplanner = models.ForeignKey(Positivity, on_delete=models.CASCADE)
    exercise_type = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exercise_type
    
class ExerciseTotalMinutes(models.Model):
    dailyplanner = models.ForeignKey(Positivity, on_delete=models.CASCADE)
    exercise_total_minutes = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'exercise total minutes'

    def __str__(self):
        return str(self.exercise_total_minutes)

    def get_exercise_total_minutes_time(self):
        return self.exercise_total_minutes
    
class ExerciseTotalSteps(models.Model):
    dailyplanner = models.ForeignKey(Positivity, on_delete=models.CASCADE)
    exercise_total_steps = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'exercise total steps'

    def __str__(self):
        return str(self.exercise_total_steps)
    
    def get_exercise_total_steps_integer(self):
        return self.exercise_total_steps
    
class ExerciseOtherInfo(models.Model):
    dailyplanner = models.ForeignKey(Positivity, on_delete=models.CASCADE)
    exercise_other_info = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'exercise other info'

    def __str__(self):
        return self.exercise_other_info
