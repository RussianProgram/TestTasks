from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

class Host(models.Model):
    ip = models.CharField(max_length=15,
                          validators=[
                              RegexValidator(
                                  regex=r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$',
                                  message='must be ip adress x.x.x.x',
                                  code='invalid ip'
                              ),
                          ])
    port = models.CharField(max_length=4,
                          validators=[
                              RegexValidator(
                                  regex=r'^\d{0,10}$',
                                  message='must be port xxxx',
                                  code='invalid port'
                              ),
                          ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owners = models.ManyToManyField(get_user_model(), related_name='hosts')

    RESOURSE_CHOICES = (
        ('windows', 'Windows'),
        ('unix', 'Unix'),
        ('sql', 'SQL')
    )

    resource = models.CharField(max_length=12,
                                choices=RESOURSE_CHOICES,
                                )

    def __str__(self):
        return f'{self.ip}:{self.port} ({self.get_owners()})'

    def get_owners(self):
        return ", ".join([o.username for o in self.owners.all()])

