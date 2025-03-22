from django.db.models import Count
from timeline.models import Timeline, Honour

def get_timeline_events():
    """Retrieve all timeline events with honour count"""
    return Timeline.objects.annotate(honour_count=Count('honours')).order_by('year')

def mark_user_honoured_events(events, user):
    """Mark events that have been honoured by the user"""
    if user.is_authenticated:
        honoured_ids = set(user.honours.values_list('timeline_id', flat=True))
        for event in events:
            event.user_has_honoured = event.id in honoured_ids
    return events

def toggle_event_honour(timeline, user):
    """Toggle honour status for a timeline event"""
    honour, created = Honour.objects.get_or_create(timeline=timeline, user=user)
    if not created:
        honour.delete()
        honoured = False
    else:
        honoured = True

    # Get updated honour count
    honour_count = timeline.honours.count()

    return {
        'honoured': honoured,
        'honour_count': honour_count
    }
