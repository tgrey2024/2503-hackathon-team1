from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


class MentorProfile(models.Model):
    """Model representing a mentor profile"""

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = CloudinaryField('image', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.role}'


class MentorContact(models.Model):
    """Model for storing mentor contact form submissions"""

    mentor_name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='mentor_contacts'
    )
    email = models.EmailField()  # Added email field
    message = models.TextField()
    submission_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('connected', 'Connected'),
            ('declined', 'Declined'),
        ],
        default='pending',
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f'Contact request for {self.mentor_name} from {self.user.username}'
        )
