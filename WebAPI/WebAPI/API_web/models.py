from django.db import models

Action_option =(
    ('wifi', 'WIFI'),
    ('shutdown', 'SHUTDOWN'),
    ('restart', 'RESTART'),
)
# Create your models here.
class Computer(models.Model):
    mac_addr = models.CharField(max_length=50,primary_key=True, unique=True)
    ip_addr = models.CharField(max_length=50, null=True, blank=True)
    isAlive = models.BooleanField(default=False)
    isBlocked = models.BooleanField(default=False)
    status = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.mac_addr

class request_action(models.Model):
    macaddr = models.ForeignKey(Computer,to_field='mac_addr', on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=Action_option)
    isStatus = models.BooleanField(default=False,blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return "{}".format(self.macaddr)

class userWifi(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username