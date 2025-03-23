from django import forms

from .models import MentorContact, MentorProfile


class MentorContactForm(forms.ModelForm):
    """Form for contacting mentors"""

    mentor_name = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        required=True,
    )

    class Meta:
        model = MentorContact
        fields = ['mentor_name', 'email', 'message']

    def clean_mentor_name(self):
        """Validate that the mentor exists if a name is provided"""
        mentor_name = self.cleaned_data.get('mentor_name')

        if (
            mentor_name
            and not MentorProfile.objects.filter(
                name__iexact=mentor_name
            ).exists()
        ):
            self.fields['mentor_name'].widget.attrs.update(
                {'class': 'form-control is-invalid'}
            )
            msg = "This mentor doesn't exist. Leave blank to find any mentor."
            raise forms.ValidationError(msg)

        return mentor_name

    def clean_email(self):
        """Validate email format"""
        email = self.cleaned_data.get('email')
        return email
