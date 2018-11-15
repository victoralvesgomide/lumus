from django.shortcuts import render, redirect
from alarm.models import Alarm
from alarm.forms import AlarmForm

# Create your views here.


def post_alarm(request):
    return render(request, 'alarm/home.html', {})

def alarms(request):
    alarms = get_all_alarm()
    form = AlarmForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('alarms')

    return render(request, 'alarm/alarm.html', {'alarms': alarms, 'form': form})

# nao ta funcionando
def delete_alarm(request, id):
    alarm = Alarm.objects.get(id=id)

    if request.method == 'POST':
        alarm.delete()
        return redirect('alarms')
    return render(request, 'alarm/delete.html', {'alarm': alarm})

def get_all_alarm():
    return Alarm.objects.all()

def get_alarm_by_id(id):
    return Alarm.objects.get(id=id)

def create_alarm(request):
    return(request, 'alarm/home.html', {})