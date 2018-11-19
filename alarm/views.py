from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from alarm.models import Alarm
from alarm.forms import AlarmForm
import datetime as dt
# Create your views here.


def post_alarm(request):
    alarms = get_all_alarm()
    nextAlarms = get_next_alarm()
    return render(request, 'alarm/home.html', {'alarms': alarms, 'nextAlarms': nextAlarms})


def alarms(request):
    alarms = get_all_alarm()
    form = AlarmForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('alarms')

    return render(request, 'alarm/alarm.html', {'alarms': alarms, 'form': form})


def delete_alarm(request, id):
    alarm = Alarm.objects.get(id=id)

    if request.method == 'POST':
        alarm.delete()
        return redirect('alarms')
    return render(request, 'alarm/delete.html', {'alarm': alarm})


def update_alarm(request, id):
    alarm = Alarm.objects.get(id=id)
    alarms = get_all_alarm()
    form = AlarmForm(request.POST or None, instance=alarm)
    if form.is_valid():
        form.save()
        return redirect('alarms')

    return render(request, 'alarm/alarm.html', {'alarms': alarms, 'form': form})


def get_all_alarm():
    return Alarm.objects.all()


def get_alarm_by_id(id):
    return Alarm.objects.get(id=id)


def get_next_alarm():
    alarms = Alarm.objects.order_by('minute').order_by('hour')
    return alarms


def snooze_alarm(request, id):
    alarm = Alarm.objects.get(id=id)
    alarm.alarm_snooze()
    print(request.META.get('HTTP_REFERER', '/'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def delete_old_alarm(request, id):
    alarm = Alarm.objects.get(id=id)
    alarm.delete()
    return redirect('post_alarm')
