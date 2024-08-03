from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *

def dailyplanners(request):
    """Display the daily planners"""
    dailyplanners = DailyPlanners.objects.order_by('-date_created')

    context = {'dailyplanners':dailyplanners}
    return render(request, 'planners/planners/dailyplanners.html', context)

def add_plan(request):
    """Adding more planners"""

    if request.method == 'POST':
        form = DailyPlannerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dailyplanners')
    else:
        form = DailyPlannerForm()

    context = {'form':form}
    return render(request, 'planners/planners/add-plan.html', context)

def dailyplanner(request, plan_id):
    """Displaying a dailyplanner"""
    daily_plan = DailyPlanners.objects.get(id=plan_id)

    # Reminder 
    reminders = daily_plan.reminder_set.order_by("-date_created")
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
    priorities = daily_plan.priority_set.order_by("-date_created")
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
    todos = daily_plan.todo_set.order_by("-date_created")
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
    exercisetypes = daily_plan.exercisetype_set.order_by("-date_created")
    if request.method == 'POST':
        exercise_type_form = ExerciseTypeForm(data=request.POST)
        if exercise_type_form.is_valid():
            new_exercise_type = exercise_type_form.save(commit=False)
            new_exercise_type.dailyplanner_id = plan_id  
            new_exercise_type.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        exercise_type_form = ExerciseTypeForm()

    exercise_total_minutes = daily_plan.exercisetotalminutes_set.order_by("-date_created")
    if request.method == 'POST':
        exercise_total_minutes_form = ExerciseTotalMinutesForm(data=request.POST)
        if exercise_total_minutes_form.is_valid():
            new_exercise_total_minutes = exercise_total_minutes_form.save(commit=False)
            new_exercise_total_minutes.dailyplanner_id = plan_id  
            new_exercise_total_minutes.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        exercise_total_minutes_form = ExerciseTotalMinutesForm()

    exercise_total_steps = daily_plan.exercisetotalsteps_set.order_by("-date_created")
    if request.method == 'POST':
        exercise_total_steps_form = ExerciseTotalStepsForm(data=request.POST)
        if exercise_total_steps_form.is_valid():
            new_exercise_total_steps = exercise_total_steps_form.save(commit=False)
            new_exercise_total_steps.dailyplanner_id = plan_id  
            new_exercise_total_steps.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        exercise_total_steps_form = ExerciseTotalStepsForm()

    exercise_other_infos = daily_plan.exerciseotherinfo_set.order_by("-date_created")
    if request.method == 'POST':
        exercise_other_info_form = ExerciseOtherInfoForm(data=request.POST)
        if exercise_other_info_form.is_valid():
            new_exercise_other_info = exercise_other_info_form.save(commit=False)
            new_exercise_other_info.dailyplanner_id = plan_id  
            new_exercise_other_info.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        exercise_other_info_form = ExerciseOtherInfoForm()

    


    # grateful
    gratefuls = daily_plan.grateful_set.order_by("-date_created")
    if request.method == 'POST':
        gratefulform = GratefulForm(data=request.POST)
        if gratefulform.is_valid():
            new_grateful = gratefulform.save(commit=False)
            new_grateful.dailyplanner_id = plan_id  
            new_grateful.save()
            return HttpResponseRedirect(f'{request.path}#grateful-form')
    else:
        gratefulform = GratefulForm()

    # Tomorrow's activities
    tomorrow_activities = daily_plan.tomorrowactivity_set.order_by("-date_created")
    if request.method == 'POST':
        tomorrowform = TomorrowForm(data=request.POST)
        if tomorrowform.is_valid():
            new_tomorrow = tomorrowform.save(commit=False)
            new_tomorrow.dailyplanner_id = plan_id  
            new_tomorrow.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        tomorrowform = TomorrowForm()

    #journals
    journals = daily_plan.journal_set.order_by("-date_created")
    if request.method == 'POST':
        journalform = JournalForm(data=request.POST)
        if journalform.is_valid():
            new_journal = journalform.save(commit=False)
            new_journal.dailyplanner_id = plan_id  
            new_journal.save()
            return redirect('dailyplanner', plan_id=plan_id)
    else:
        journalform = JournalForm()
    


    context = {
        'daily_plan':daily_plan,

        "reminders": reminders,
        'reminderform': reminderform,

        "priorities": priorities,
        "priorityform": priorityform,

        "todos": todos,
        "todoform": todoform,
        "total_todos": total_todos,
        "completed_todos": completed_todos,
        "uncompleted_todos": uncompleted_todos,

        "gratefuls": gratefuls,
        "gratefulform": gratefulform,

        "tomorrow_activities": tomorrow_activities,
        "tomorrowform": tomorrowform,

        "journals": journals,
        "journalform": journalform,

        "exercisetypes": exercisetypes,
        "exercise_type_form": exercise_type_form,

        "exercise_total_minutes": exercise_total_minutes,
        "exercise_total_minutes_form": exercise_total_minutes_form,

        "exercise_total_steps": exercise_total_steps,
        "exercise_total_steps_form": exercise_total_steps_form,

        "exercise_other_infos": exercise_other_infos,
        "exercise_other_info_form": exercise_other_info_form,

        }
    return render(request, 'planners/planners/dailyplanner.html', context)