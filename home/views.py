from django.shortcuts import render
from timeline.models import Timeline

def home(request):
    # Get ALL timeline events, sorted by year
    timeline_events = Timeline.objects.all().order_by('-year')
    
    context = {
        'timeline_events': timeline_events
    }
    return render(request, 'home/index.html')


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')