from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=30)
    uploadTime = models.TimeField((u"Conversation Time"), auto_now_add=True, blank=True)

    def __str__(self):
        return "id:" + str(self.id) + ", file: " + self.name + ", UploadedOn: " + str(self.uploadTime)

class Data(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return "[file:"+self.file.name+", x:"+str(self.x)+", y:"+str(self.y)+"]"