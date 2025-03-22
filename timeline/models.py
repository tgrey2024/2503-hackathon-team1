from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Timeline(models.Model):
    """Represents a historical event honoring women in tech"""
    event = models.CharField(max_length=255, help_text="Enter the name of the event")
    description = models.TextField(help_text="Enter a description of the event")
    year = models.IntegerField(help_text="Enter the year (YYYY)")
    image = CloudinaryField('image', null=True, blank=True, help_text="Upload an image related to the event")

    def __str__(self):
        return f"{self.event} ({self.year})"

class Honour(models.Model):
    """Represents a user's honouring of a timeline event"""
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE, related_name='honours')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='honours')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['timeline', 'user'], name='unique_timeline_user')
        ]

    def __str__(self):
        return f"{self.user.username} honoured {self.timeline.event}"
