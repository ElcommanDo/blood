from django.db import models
from form.models import Doner
# Create your models here.


class Request(models.Model):
    doner = models.ForeignKey(Doner, on_delete=models.CASCADE, related_name='doner')
    user = models.ForeignKey(Doner, on_delete=models.CASCADE, related_name='requested')
    case = models.BooleanField(null=True, default='UnKnown')


