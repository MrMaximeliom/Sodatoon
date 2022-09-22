from django.db import models
from utils.constants import LIKE_REACTIONS


class EpisodeLike(models.Model):
    episode = models.ForeignKey(
        "episodes.Episode",
        on_delete=models.CASCADE,
        null=False,
        blank=False

    )
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    like_reaction = models.CharField(
        choices=LIKE_REACTIONS,
        null=False,
        blank=False,
        max_length=100
    )
    like_datetime = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )


