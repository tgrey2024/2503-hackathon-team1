from django.shortcuts import render

from utils.timeline import get_timeline_events, mark_user_honoured_events


def index(request):
    """
    View for the home page that includes timeline events
    """
    # Fetch timeline events using the same utility function used by the timeline view
    timeline_events = get_timeline_events()
  
    # Limit to only 3 timeline events
    timeline_events = timeline_events[:3]

    # Mark events that have been honoured by the current user
    timeline_events = mark_user_honoured_events(timeline_events, request.user)

    context = {
        'timeline_events': timeline_events,
    }

    return render(request, 'home/index.html', context)
