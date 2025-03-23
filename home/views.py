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
    members = [
        {
            'name': 'Deborah_Alumni',
            'role': 'Hackathon Veteran',
            'bio': 'Deborah is an experienced hackathon alumnus with a passion for continuous learning.',
            'image': 'home/images/debbiect246j.jpg',
            'github': 'https://github.com/deborah-alumni'
        },
        {
            'name': 'Ashwin',
            'role': 'Hackathon Veteran',
            'bio': 'Ashwin brings innovative ideas and strong technical skills to every project.',
            'image': 'home/images/ashwin.jpg',
            'github': 'https://github.com/tgrey2024'
        },
        {
            'name': 'Kiree_Alumni',
            'role': 'Hackathon Veteran',
            'bio': 'Kiree is an alumni with extensive knowledge in front-end and user experience design.',
            'image': 'home/images/kiree.jpg',
            'github': 'https://github.com/kiree-alumni'
        },
        {
            'name': 'Linus J',
            'role': 'Hackathon Veteran',
            'bio': 'Linus specializes in problem-solving and agile workflows, ensuring smooth collaboration.',
            'image': 'home/images/linusj.jpg',
            'github': 'https://github.com/linus-j'
        },
        {
            'name': 'Vital_SP',
            'role': 'Hackathon Veteran',
            'bio': 'Vital is known for his leadership and back-end expertise, always pushing projects forward.',
            'image': 'home/images/vinsengi.png',
            'github': 'https://github.com/vital-sp'
        },
        {
            'name': 'Tripta_BC',
            'role': 'Hackathon Veteran',
            'bio': 'Tripta excels in brainstorming innovative solutions and fostering team synergy...',
            'image': 'home/images/tripta.jpg',
            'github': 'https://github.com/tripta-bc'
        },
    ]

    return render(request, 'home/about.html', {'members': members})