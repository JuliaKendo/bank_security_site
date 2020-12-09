from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self, visit):
        leaved_at = visit.leaved_at if visit.leaved_at else localtime()
        time_stay_in_vault = leaved_at - localtime(visit.entered_at)
        return time_stay_in_vault.total_seconds()

    def format_duration(self, visit_duration_seconds):
        hours = int(visit_duration_seconds // 3600)
        minutes = int((visit_duration_seconds % 3600) // 60)
        seconds = int(visit_duration_seconds - ((hours * 3600) + (minutes * 60)))
        return f'{hours}:{minutes}:{seconds}'

    def is_visit_long(self, visit, duration_of_long_visit):
        visit_duration_seconds = self.get_duration(visit)
        if int(visit_duration_seconds // 60) >= duration_of_long_visit:
            return True
