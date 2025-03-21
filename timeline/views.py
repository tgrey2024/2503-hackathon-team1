from django.shortcuts import render
from .models import Timeline

def timeline(request):
    events = Timeline.objects.all().order_by('year')
    return render(request, 'timeline/timeline.html', {'events': events})
