from django.shortcuts import render, redirect
from .models import *
from .forms import *

def dailyplanners(request):
    """Display the daily planners"""
    dailyplanners = Positivity.objects.order_by('-date_created')

    context = {'dailyplanners':dailyplanners}
    return render(request, 'planner/planners/dailyplanners.html', context)

def positivity(request):
    """Add more positivity"""
    if request.method == 'POST':
        form = PositivityForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dailyplanners')
    else:
        form = PositivityForm()

    context = {'form':form}
    return render(request, 'planner/planners/positivity.html', context)

def dailyplanner(request, plan_id):
    """Display the daily planner"""
    dailyplan = Positivity.objects.get(id=plan_id)

    reminders = dailyplan.reminder_set.order_by("-date_created")
    if request.method == 'POST':
        reminderform = ReminderForm(data=request.POST)
        if reminderform.is_valid():
            new_reminder = reminderform.save(commit=False)
            new_reminder.dailyplanner_id = plan_id  # Set the foreign key
            new_reminder.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        reminderform = ReminderForm()

    # Priorities
    priorities = dailyplan.priority_set.order_by("-date_created")
    if request.method == 'POST':
        priorityform = PriorityForm(data=request.POST)
        if priorityform.is_valid():
            new_priority = priorityform.save(commit=False)
            new_priority.dailyplanner_id = plan_id  # Set the foreign key
            new_priority.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        priorityform = PriorityForm()
    
    # todos 
    todos = dailyplan.todo_set.order_by("-date_created")
    total_todos = todos.count()
    completed = todos.filter(completed=True)
    completed_todos = completed.count()
    uncompleted_todos = total_todos - completed_todos
    if request.method == 'POST':
        todoform = ToDoForm(data=request.POST)
        if todoform.is_valid():
            new_todo = todoform.save(commit=False)
            new_todo.dailyplanner_id = plan_id  # Set the foreign key
            new_todo.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        todoform = ToDoForm()


    # Exercise
    exercisetypes = dailyplan.exercisetype_set.order_by("-date_created")
    if request.method == 'POST':
        exercise_type_form = ExerciseTypeForm(data=request.POST)
        if exercise_type_form.is_valid():
            new_exercise_type = exercise_type_form.save(commit=False)
            new_exercise_type.dailyplanner_id = plan_id  
            new_exercise_type.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        exercise_type_form = ExerciseTypeForm()

    exercise_total_minutes = dailyplan.exercisetotalminutes_set.order_by("-date_created")
    if request.method == 'POST':
        exercise_total_minutes_form = ExerciseTotalMinutesForm(data=request.POST)
        if exercise_total_minutes_form.is_valid():
            new_exercise_total_minutes = exercise_total_minutes_form.save(commit=False)
            new_exercise_total_minutes.dailyplanner_id = plan_id  
            new_exercise_total_minutes.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        exercise_total_minutes_form = ExerciseTotalMinutesForm()

    exercise_total_steps = dailyplan.exercisetotalsteps_set.order_by("-date_created")
    if request.method == 'POST':
        exercise_total_steps_form = ExerciseTotalStepsForm(data=request.POST)
        if exercise_total_steps_form.is_valid():
            new_exercise_total_steps = exercise_total_steps_form.save(commit=False)
            new_exercise_total_steps.dailyplanner_id = plan_id  
            new_exercise_total_steps.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        exercise_total_steps_form = ExerciseTotalStepsForm()

    exercise_other_infos = dailyplan.exerciseotherinfo_set.order_by("-date_created")
    if request.method == 'POST':
        exercise_other_info_form = ExerciseOtherInfoForm(data=request.POST)
        if exercise_other_info_form.is_valid():
            new_exercise_other_info = exercise_other_info_form.save(commit=False)
            new_exercise_other_info.dailyplanner_id = plan_id  
            new_exercise_other_info.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        exercise_other_info_form = ExerciseOtherInfoForm()

    



    context = {
        'dailyplan': dailyplan,

        'reminders': reminders,
        'reminderform': reminderform,

        'priorities': priorities,
        'priorityform': priorityform,

        "todos": todos,
        "todoform": todoform,
        "total_todos": total_todos,
        "completed_todos": completed_todos,
        "uncompleted_todos": uncompleted_todos,

        "exercisetypes": exercisetypes,
        "exercise_type_form": exercise_type_form,

        "exercise_total_minutes": exercise_total_minutes,
        "exercise_total_minutes_form": exercise_total_minutes_form,

        "exercise_total_steps": exercise_total_steps,
        "exercise_total_steps_form": exercise_total_steps_form,

        "exercise_other_infos": exercise_other_infos,
        "exercise_other_info_form": exercise_other_info_form,
    }
    return render(request, 'planner/planners/dailyplanner.html', context)