from django.shortcuts import render
from utils.timeline import get_timeline_events, mark_user_honoured_events

def index(request):
    """Display the home page with timeline events"""
    # Get timeline events using the utility function
    timeline_events = get_timeline_events()
    
    # Mark events that the current user has honoured
    timeline_events = mark_user_honoured_events(timeline_events, request.user)
    
    return render(request, 'home/index.html', {
        'timeline_events': timeline_events
    })


def index(request):
    return render(request, 'home/index.html')

def about(request):
    members = [
        {
            'name': 'Deborah_Alumni',
            'role': 'Hackathon Veteran',
            'bio': 'Deborah is an experienced hackathon alumnus with a passion for continuous learning.',
            'image': 'home/images/debbiect246.webp',
            'github': 'https://github.com/debbiect246'
        },
        {
            'name': 'Ashwin',
            'role': 'Hackathon Veteran',
            'bio': 'Ashwin brings innovative ideas and strong technical skills to every project.',
            'image': 'home/images/ashwin.webp',
            'github': 'https://github.com/ashwinsel'
        },
        {
            'name': 'Kiree_Alumni',
            'role': 'Hackathon Veteran',
            'bio': 'Kiree is an alumni with extensive knowledge in front-end and user experience design.',
            'image': 'home/images/swewi.webp',
            'github': 'https://github.com/swewi'
        },
        {
            'name': 'Linus J',
            'role': 'Hackathon Veteran',
            'bio': 'Linus specializes in problem-solving and agile workflows, ensuring smooth collaboration.',
            'image': 'home/images/j0hanz.webp',
            'github': 'https://github.com/j0hanz'
        },
        {
            'name': 'Vital_SP',
            'role': 'Hackathon Veteran',
            'bio': 'Vital is known for his leadership and back-end expertise, always pushing projects forward.',
            'image': 'home/images/vinsengi.webp',
            'github': 'https://github.com/vinsengi'
        },
        {
            'name': 'Tripta_BC',
            'role': 'Hackathon Veteran',
            'bio': 'Tripta excels in brainstorming innovative solutions and fostering team synergy...',
            'image': 'home/images/tgrey2024.webp',
            'github': 'https://github.com/tgrey2024'
        },
    ]

    return render(request, 'home/about.html', {'members': members})
