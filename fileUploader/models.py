from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=30)
    uploadTime = models.TimeField((u"Conversation Time"), auto_now_add=True, blank=True)

class Data(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()