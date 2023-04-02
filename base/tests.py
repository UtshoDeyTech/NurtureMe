from django.test import TestCase
from django.urls import reverse
from .models import Room, Question, Option, CustomUser


class TestViews(TestCase):
    def setUp(self):
        self.room = Room.objects.create(FormName='Test Room')
        self.question = Question.objects.create(room=self.room, question='Test Question', marks=10)
        self.option = Option.objects.create(question=self.question, option='Test Option', mark=5, note='Test Note')
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='password')

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302) # since login is required for home page access, it will redirect to login page
        self.client.login(username='testuser', password='password')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_room_view(self):
        url = reverse('room', args=[str(self.room.uid)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302) # since login is required for room page access, it will redirect to login page
        self.client.login(username='testuser', password='password')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'room.html')

    def test_survey_view(self):
        url = reverse('survey')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302) # since login is required for survey page access, it will redirect to login page
        self.client.login(username='testuser', password='password')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'survey.html')

    def test_signup_view(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_view(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class TestModels(TestCase):
    def setUp(self):
        self.room = Room.objects.create(FormName='Test Room')
        self.question = Question.objects.create(room=self.room, question='Test Question', marks=10)
        self.option = Option.objects.create(question=self.question, option='Test Option', mark=5, note='Test Note')
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='password')

    def test_room_model(self):
        self.assertEqual(str(self.room), 'Test Room')

    def test_question_model(self):
        self.assertEqual(str(self.question), 'Test Question')

    def test_option_model(self):
        self.assertEqual(str(self.option), 'Test Option')

    def test_customuser_model(self):
        self.assertEqual(str(self.user), 'testuser')
        self.assertFalse(self.user.is_filled)
        self.assertEqual(self.user.mark, 0)
        self.assertEqual(self.user.evaluation, '')
