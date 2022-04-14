from django.db import models
from apps.accounts.models import User

"""
Event Model:
this model is used to save event's data
"""
class Event(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(blank=False, null=False)
    event_description = models.TextField(blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table='event'
"""
Event Participants Model:
this model is used to save events participants data
"""
class EventParticipants(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    participating_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.event_id.title + str(self.user_id.username)

    class Meta:
        db_table = 'event_participant'