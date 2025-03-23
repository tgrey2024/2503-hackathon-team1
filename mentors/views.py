from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MentorContactForm
from .models import MentorProfile


def mentor_list(request):
    """Display list of available mentors"""
    mentors = MentorProfile.objects.all()[:3]  # Get only 3 mentors for display
    return render(request, 'mentors/mentors.html', {'mentors': mentors})


@login_required
def contact_form(request, mentor_id=None):
    """Display and process the mentor contact form"""
    initial_data = {}
    if mentor_id:
        mentor = get_object_or_404(MentorProfile, id=mentor_id)
        initial_data = {'mentor_name': mentor.name}

    if request.method == 'POST':
        form = MentorContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()

            messages.success(
                request, 'Your request has been submitted successfully!'
            )
            return redirect('mentors:contact_success')
    else:
        form = MentorContactForm(initial=initial_data)

    return render(request, 'mentors/contact_form.html', {'form': form})


@login_required
def contact_success(request):
    """Display successful form submission confirmation"""
    return render(request, 'mentors/contact_success.html')
