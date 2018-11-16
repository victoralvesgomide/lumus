from django import forms
from alarm.models import Alarm

class AlarmForm(forms.ModelForm):
    
    class Meta:
        model = Alarm
        fields = ['hour', 'minute', 'comment', 'link_video', 'is_enable']
        