from django.test import TestCase
from django.contrib.auth import get_user_model
from sgce.core.models import Profile


class ProfileModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user('user', 'user@mail.com', 'pass')
        # When a user is created a profile is created too.
        self.profile = user.profile

    def test_create(self):
        self.assertTrue(Profile.objects.exists())

    def test_phone_can_be_blank(self):
        field = Profile._meta.get_field('phone')
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual('Perfil de {}'.format(self.profile.user.get_full_name()), str(self.profile))

    def test_role_default_to_common_user(self):
        """By default must be 'u' (Profile.USER)"""
        self.assertEqual(self.profile.role, Profile.USER)