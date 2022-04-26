from django.db import models

Action_option =(
    ('noAction', 'NOACTION'),
    ('shutdown', 'SHUTDOWN'),
    ('restart', 'RESTART'),
)
# Create your models here.
class Computer(models.Model):
    mac_addr = models.CharField(max_length=50, unique=True)
    isActive = models.BooleanField(default=False)
    isConnected = models.BooleanField(default=False)
    isBlocked = models.BooleanField(default=False)
    isAction = models.CharField(max_length=50, default=False, null=True, choices=Action_option)
    note = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.mac_addr

class userWifi(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username