from django.db import models
from model_utils.models import TimeStampedModel

from birdman.core.validators import rating_validator


class UserVisit(TimeStampedModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    cowork = models.ForeignKey('cowork.Cowork', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=(rating_validator,))

    def __str__(self):
        return "{} in {} ({})".format(self.user, self.cowork, self.created)

    class Meta:
        ordering = ('-created',)
