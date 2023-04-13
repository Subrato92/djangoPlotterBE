from django.db import models

# Create your models here.
class FileX(models.Model):
    name = models.CharField(max_length=30)
    uploadTime = models.TimeField((u"Conversation Time"), auto_now_add=True, blank=True)

class DataY(models.Model):
    file = models.ForeignKey(FileX, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()