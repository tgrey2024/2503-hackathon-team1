from django.shortcuts import render
from utils.timeline import get_timeline_events, mark_user_honoured_events

from django.shortcuts import render
from utils.timeline import get_timeline_events, mark_user_honoured_events

def index(request):
    """
    View for the home page that includes timeline events
    """
    # Fetch timeline events using the same utility function used by the timeline view
    timeline_events = get_timeline_events()
    
    # Mark events that have been honoured by the current user
    timeline_events = mark_user_honoured_events(timeline_events, request.user)
    
    context = {
        'timeline_events': timeline_events,
    }
    
    return render(request, 'home/index.html', context)


def about(request):
    members = [
        {
            'name': 'Deborah_Alumni',
            'role': 'Hackathon Veteran',
            'bio': 'Deborah is an experienced hackathon alumnus with a passion for continuous learning.',
            'image': 'home/images/debbiect246.jpg',
            'github': 'https://github.com/debbiect246'
        },
        {
            'name': 'Ashwin',
            'role': 'Hackathon Veteran',
            'bio': 'Ashwin brings innovative ideas and strong technical skills to every project.',
            'image': 'home/images/ashwin.jpg',
            'github': 'https://github.com/ashwinsel'
        },
        {
            'name': 'Kiree_Alumni',
            'role': 'Hackathon Veteran',
            'bio': 'Kiree is an alumni with extensive knowledge in front-end and user experience design.',
            'image': 'home/images/swewi.jpg',
            'github': 'https://github.com/swewi'
        },
        {
            'name': 'Linus J',
            'role': 'Hackathon Veteran',
            'bio': 'Linus specializes in problem-solving and agile workflows, ensuring smooth collaboration.',
            'image': 'home/images/j0hanz.jpg',
            'github': 'https://github.com/j0hanz'
        },
        {
            'name': 'Vital_SP',
            'role': 'Hackathon Veteran',
            'bio': 'Vital is known for his leadership and back-end expertise, always pushing projects forward.',
            'image': 'home/images/vinsengi.png',
            'github': 'https://github.com/vinsengi'
        },
        {
            'name': 'Tripta_BC',
            'role': 'Hackathon Veteran',
            'bio': 'Tripta excels in brainstorming innovative solutions and fostering team synergy...',
            'image': 'home/images/tgrey2024.jpg',
            'github': 'https://github.com/tgrey2024'
        },
    ]

    return render(request, 'home/about.html', {'members': members})
