from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils import Choices
from model_utils.models import StatusModel, TimeStampedModel


class VisitRequest(StatusModel, TimeStampedModel):
    requesting_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cowork = models.ForeignKey('cowork.Cowork', on_delete=models.CASCADE)
    start_day = models.DateField()
    end_day = models.DateField()
    STATUS = Choices('PENDING', 'CONFIRMED', 'DECLINED')

    def __str__(self):
        return "{} to {} ({})".format(self.requesting_user, self.cowork, self.status)


@receiver(post_save, sender=VisitRequest, dispatch_uid="change_visit_status")
def send_status_update_notification(instance=None, created=False, *args, **kwargs):
    if instance.status_changed:
        """
        TODO - ping notifications service to send push
        """
        pass
