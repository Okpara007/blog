from django.test import TestCase
from .models import Author

class AuthorModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Johnathan Moore", email="johnathan@example.com", bio="An AI writer")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "Johnathan Moore")
        self.assertEqual(self.author.email, "johnathan@example.com")
        self.assertEqual(self.author.bio, "An AI writer")
