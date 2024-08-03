from django import forms 
from django.forms import ModelForm
from .models import *


class PositivityForm(forms.ModelForm):
    class Meta:
        model = Positivity
        fields = ['quote', 'affirmation']
        widgets = {
            'quote': forms.Textarea(attrs={'rows':10, 'cols':70, "placeholder":"Quote of the day..."}),
            'affirmation': forms.Textarea(attrs={'rows':10, 'cols':70, "placeholder":"Affirmation..."})
        }

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['reminder']
        widgets = {
            'reminder': forms.TextInput(attrs={'class': 'planner-input', "placeholder":"Remember to..."}),
        }

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['priority']
        widgets = {
            'priority': forms.TextInput(attrs={'class': 'planner-input', "placeholder":"I purpose to..."}),
        }

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['todo']
        widgets = {
            'todo': forms.TextInput(attrs={'class': 'todo-input', "placeholder":"Write your to do here.."}),
        }

class ExerciseTypeForm(forms.ModelForm):
    class Meta:
        model = ExerciseType
        fields = ['exercise_type']
        widgets = {
            'exercise_type': forms.TextInput(attrs={'class': 'planner-input', "placeholder":"Exercise Type..."}),
        }
class ExerciseTotalMinutesForm(forms.ModelForm):
    class Meta:
        model = ExerciseTotalMinutes
        fields = ['exercise_total_minutes']
        widgets = {
            'exercise_total_minutes': forms.TimeInput(attrs={'class': 'planner-input', "placeholder": "HH:MM:SS"}),
        }
class ExerciseTotalStepsForm(forms.ModelForm):
    class Meta:
        model = ExerciseTotalSteps
        fields = ['exercise_total_steps']
        widgets = {
            'exercise_total_steps': forms.TextInput(attrs={'class': 'planner-input', "placeholder":"Number of steps today..."}),
        }
class ExerciseOtherInfoForm(forms.ModelForm):
    class Meta:
        model = ExerciseOtherInfo
        fields = ['exercise_other_info']
        widgets = {
            'exercise_other_info': forms.Textarea(attrs={'rows':5, 'cols':30, "placeholder":"Note to self on exercise..."}),
        }
