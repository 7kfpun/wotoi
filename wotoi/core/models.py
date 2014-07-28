from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):

    USER_TYPE = (
        ('S', 'Seeker'),
        ('E', 'Employer'),
    )

    user = models.OneToOneField(User)

    user_type = models.CharField(max_length=1, choices=USER_TYPE)
