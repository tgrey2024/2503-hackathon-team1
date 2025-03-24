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


def about(request):
    members = [
        {
            'name': 'Deborah Thompson',
            'role': 'Hackathon Veteran',
            'bio': 'Deborah is an experienced hackathon alumnus with a passion for continuous learning.',
            'image': 'images/debbiect246.webp',
            'github': 'https://github.com/debbiect246',
            'linkedIn': 'https://www.linkedin.com/in/debbie-thompson-1baa4733/',
        },
        {
            'name': 'Ashwinkarthik Selvaraj',
            'role': 'Hackathon Veteran',
            'bio': 'Ashwin brings innovative ideas and strong technical skills to every project.',
            'image': 'images/ashwin.webp',
            'github': 'https://github.com/ashwinsel',
            'linkedIn': 'https://www.linkedin.com/in/ashwinkarthik-selvaraj-12882751/',
        },
        {
            'name': 'Kiree Bellamy',
            'role': 'Hackathon Veteran',
            'bio': 'Kiree is an alumnus with extensive knowledge in front-end and user experience design.',
            'image': 'images/swewi.webp',
            'github': 'https://github.com/swewi',
            'linkedin': 'https://www.linkedin.com/in/kireebellamy/',
        },
        {
            'name': 'Linus Johansson',
            'role': 'Hackathon Veteran',
            'bio': 'Linus specialises in problem-solving and agile workflows, ensuring smooth collaboration.',
            'image': 'images/j0hanz.webp',
            'github': 'https://github.com/j0hanz',
            'linkedIn': 'https://www.linkedin.com/in/linus-johansson-software-dev/',
        },
        {
            'name': 'Vital Nsengiyumva',
            'role': 'Hackathon Veteran',
            'bio': 'Vital is known for his leadership and back-end expertise, always pushing projects forward.',
            'image': 'images/vinsengi.webp',
            'github': 'https://github.com/vinsengi',
            'linkedIn': 'https://www.linkedin.com/in/vital-nsengiyumva/',
        },
        {
            'name': 'Tripta Grey',
            'role': 'Hackathon Veteran',
            'bio': 'Tripta excels in brainstorming innovative solutions and fostering team synergy.',
            'image': 'images/tgrey2024.webp',
            'github': 'https://github.com/tgrey2024',
            'linkedIn': 'https://www.linkedin.com/in/triptagrey/',
        },
    ]

    return render(request, 'home/about.html', {'members': members})
