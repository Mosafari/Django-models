from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class internet_seesion(models.Model):
    name = models.CharField(_("name"),max_length=255)
    start_time = models.CharField(_("start time"),max_length=255)
    usage_time = models.CharField(_("usage time"),max_length=255)
    ip = models.CharField(_("ip"),max_length=255)
    MAC = models.CharField(_("MAC"),max_length=255)
    upload = models.FloatField(_("upload"))
    download = models.FloatField(_("download"))
    total_transfers = models.FloatField(_("total transfers"))
    session_break_reason = models.CharField(_("session break reason"),max_length=255)