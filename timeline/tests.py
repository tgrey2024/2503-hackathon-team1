from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Timeline, Honour

class TimelineHonourTests(TestCase):
    def setUp(self):
        # Set up test user, timeline entry, and client
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.timeline = Timeline.objects.create(
            event='Test Event',
            description='Test Description',
            year=2023
        )

        self.client = Client()

    def test_honour_authentication_required(self):
        """Verify unauthenticated requests are redirected without creating honours"""
        response = self.client.post(
            reverse('timeline:toggle_honour', args=[self.timeline.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Honour.objects.count(), 0)

    def test_honour_toggle(self):
        """Verify honour can be added and removed by authenticated users"""
        # Authenticate user
        self.client.login(username='testuser', password='testpassword')

        # First request should create honour
        response = self.client.post(
            reverse('timeline:toggle_honour', args=[self.timeline.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Honour.objects.count(), 1)

        # Second request should remove honour
        response = self.client.post(
            reverse('timeline:toggle_honour', args=[self.timeline.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Honour.objects.count(), 0)

    def test_honour_count(self):
        """Verify honour count in response reflects database state"""
        # Add honour as first user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('timeline:toggle_honour', args=[self.timeline.id])
        )
        data = response.json()
        self.assertEqual(data['honour_count'], 1)

        # Add second user's honour independently
        user2 = User.objects.create_user(
            username='testuser2',
            password='testpassword'
        )
        Honour.objects.create(user=user2, timeline=self.timeline)

        # Remove first user's honour, count should be 1
        response = self.client.post(
            reverse('timeline:toggle_honour', args=[self.timeline.id])
        )
        data = response.json()
        self.assertEqual(data['honour_count'], 1)
