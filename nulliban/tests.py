from django.test import TestCase

# Create your tests here.
from nulliban.models import NullIban


class NullIbanTest(TestCase):
    def test_null_iban_field(self):
        iban = NullIban()
        iban.save()
