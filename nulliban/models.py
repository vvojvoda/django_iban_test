from django.db import models
from django_iban.fields import IBANField


class NullIban(models.Model):
    iban = IBANField(null=True, blank=True)