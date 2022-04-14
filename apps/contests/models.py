from django.db import models
from apps.accounts.models import User

"""
Contest Model:
this model is used to save contest's data
"""
class Contest(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(blank=False, null=False)
    prize = models.TextField(blank=True, null=True)
    starting_timestamp = models.DateTimeField(null=True, blank=True)
    ending_timestamp = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'contest'



"""
Contest Participants Model:
this model is used to save events participants data
"""
class ContestParticipants(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    contest_id = models.ForeignKey(Contest, on_delete=models.CASCADE)
    participating_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.contest_id.title + str(self.user_id.username)

    class Meta:
        db_table = 'contest_participant'