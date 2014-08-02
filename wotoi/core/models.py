from django.contrib.auth.models import AbstractUser
from django.db import models


class Skill(models.Model):

    name = models.CharField(max_length=20)

    # endorsements = models.ManyToManyField(User)


class Language(models.Model):

    alpha2 = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    # endorsements = models.ManyToManyField(User)


class Experience(models.Model):

    name = models.CharField(max_length=20)

    # endorsements = models.ManyToManyField(User)


# class TranslateLanguage(models.Model):

    # language_from = models.ForeignKey(Language)
    # language_to = models.ForeignKey(Language)

    # endorsements = models.ManyToManyField(User)


class CustomUser(AbstractUser):

    USER_TYPE = (
        ('SEEKER', 'Seeker'),
        ('EMPLOYER', 'Employer'),
    )

    # COMPANY_TYPE = (
    #     ('AGENCY', 'Agency'),
    #     ('INDIVIDUAL', 'Individual company'),
    # )

    is_approved = models.BooleanField(default=False)

    user_type = models.CharField(max_length=20, choices=USER_TYPE)

    # profile_picture = models.ImageField()
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    # Employer
    # company_type = models.CharField(max_length=20, choices=COMPANY_TYPE)
    # company_name = models.CharField(max_length=256)
    # registration_number = models.CharField(max_length=256)
    # address = models.TextField()

    # Seeker
    skills = models.ForeignKey(Skill, null=True)
    languages = models.ForeignKey(Language, null=True)
    experiences = models.ManyToManyField(Experience, null=True)

    # followers = models.ManyToManyField(
    # 'self', related_name='followees', symmetrical=False)

    def __unicode__(self):
        return '%s - %s' % (self.username, self.user_type)


class Job(models.Model):

    CATEGORY_TYPE = (
        ('TRANSLATE', 'Translate'),
        ('COPYWRITE', 'copywrite'),
        ('PROOFREAD', 'proofread'),
        ('INTERPRET', 'interpret'),
    )

    UNIT_TYPE = (
        ('WORD', 'Word'),
        ('PROJECT', 'Project'),
        ('HOUR', 'Hour'),
        ('DAY', 'Day'),
    )

    title = models.CharField(max_length=256)
    category = models.CharField(max_length=20, choices=CATEGORY_TYPE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    unit = models.CharField(max_length=20, choices=UNIT_TYPE)
    until_date = models.DateField(blank=True)

    languages = models.ManyToManyField(Language)
    # translate_language = models.ManyToManyField(TranslateLanguage)

    is_approved = models.BooleanField(default=False)

    user = models.ForeignKey(CustomUser)

    def __unicode__(self):
        return '%s - %s, %s' % (self.title, self.category, self.user.username)

    def all_languages(self):
        return list(self.languages.all())


class CandidateTest(models.Model):

    description = models.TextField()
    requirements = models.TextField()

    job = models.ForeignKey(Job)


class CandidateAnswer(models.Model):
    # answer = autofield

    answer = models.TextField()

    user = models.ForeignKey(CustomUser)
    candidate_test = models.ForeignKey(CandidateTest)
