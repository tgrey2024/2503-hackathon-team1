from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Timeline
from utils.timeline import get_timeline_events, mark_user_honoured_events, toggle_event_honour

def timeline(request: HttpRequest) -> HttpResponse:
    """Display timeline of events"""
    events = get_timeline_events()
    events = mark_user_honoured_events(events, request.user)
    return render(request, 'timeline/timeline.html', {'events': events})

@login_required
def toggle_honour(request: HttpRequest, timeline_id: int) -> JsonResponse:
    """Toggle honour status of an event"""
    if request.method != 'POST':
        return JsonResponse({"error": "Method not allowed"}, status=405)

    timeline = get_object_or_404(Timeline, id=timeline_id)
    result = toggle_event_honour(timeline, request.user)
    return JsonResponse(result)
