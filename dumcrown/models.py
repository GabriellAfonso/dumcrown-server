from django.contrib.auth.models import User
from django.db import models


class LoginHistory(models.model):
    player = models.ForeignKey(User, models.DO_NOTHING)
    login_time = models.DateTimeField(auto_now_add=True)


class Player(models.model):
    user = models.OneToOneField(User, models.DO_NOTHING)
    nickname = models.CharField(max_length=25, blank=True, default='')
    avatar = models.CharField(max_length=25, blank=True, default='')
    border = models.CharField(max_length=25, blank=True, default='')
    rank = models.CharField(max_length=25, blank=True, default='')
    rank_points = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=1)
    experience = models.PositiveBigIntegerField(default=0)
    date_of_birth = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def record_login(self):
        LoginHistory.objects.create(player=self)
        last_login_record = LoginHistory.objects.filter(
            player=self).order_by('-login_time').first()
        if last_login_record:
            self.last_login = last_login_record.login_time
            self.save()
