from django.shortcuts import render

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
            'bio': 'Kiree is an alumni with extensive knowledge in front-end and user experience design.',
            'image': 'images/swewi.webp',
            'github': 'https://github.com/swewi',
            'linkedIn': 'https://www.linkedin.com/in/kireebellamy/',
        },
        {
            'name': 'Linus Johansson',
            'role': 'Hackathon Veteran',
            'bio': 'Linus specializes in problem-solving and agile workflows, ensuring smooth collaboration.',
            'image': 'images/j0hanz.webp',
            'github': 'https://github.com/j0hanz',
            'linkedIn': 'https://www.linkedin.com/in/linus-johansson-software-dev/',
        },
        {
            'name': 'Vital Nsengiyumva',
            'role': 'Hackathon Newbie',
            'bio': 'Vital is known for his leadership and back-end expertise, always pushing projects forward.',
            'image': 'images/vinsengi.webp',
            'github': 'https://github.com/vinsengi',
            'linkedIn': 'https://www.linkedin.com/in/vital-nsengiyumva/',
        },
        {
            'name': 'Tripta Grey',
            'role': 'Hackathon Newbie',
            'bio': 'Tripta excels in brainstorming innovative solutions and fostering team synergy.',
            'image': 'images/tgrey2024.webp',
            'github': 'https://github.com/tgrey2024',
            'linkedIn': 'https://www.linkedin.com/in/triptagrey/',
        },
    ]

    return render(request, 'about/about.html', {'members': members})

