from django.test import TestCase
from django.contrib.auth.models import BaseUserManager
from .models import CustomUser, CustomUserManager


class CustomUserManagerTests(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.first_name = "Test"
        self.last_name = "User"
        self.email = "<EMAIL>"
        self.password = "password"
        self.extra_fields = {"is_staff": False, "is_superuser": False}
        self.user_manager = CustomUserManager()

    def test_create_user(self):
        user = self.user_manager.create_user(
            self.username, self.first_name, self.last_name, self.email, self.password, **self.extra_fields
        )
        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.first_name, self.first_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        manager = CustomUserManager()
        user = manager.create_superuser(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='<EMAIL>',
            password='password'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
