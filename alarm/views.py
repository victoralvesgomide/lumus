from django.shortcuts import render

# Create your views here.


def post_alarm(request):
    return render(request, 'alarm/home.html', {})
