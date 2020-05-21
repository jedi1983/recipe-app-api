from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@test.com', password='testpass'):
    """Create a Sample User"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test Creating user with email is successfull"""
        email = "ragunan@hotmail.com"
        password = "passTest123"
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test thet email domain name"""
        email = "roland@HOTMAIL.com"
        user = get_user_model().objects.create_user(email=email,
                                                    password="test123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Testing email user invalid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test Creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'roland@hotmail.com',
            'pass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test Tag String Reprentation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """ test ingredient string representation """
        ingredient = models.Ingredient.objects.create(
                user=sample_user(),
                name='Cucumber'
            )

        self.assertEqual(str(ingredient), ingredient.name)
